#!/usr/bin/env python3
"""Baja los boletines de NESTOR y construye un índice buscable de bibliografía egea.

NESTOR (Universidad de Cincinnati) es la bibliografía internacional de estudios egeos:
mensual, gratuita, y con cobertura de Lineal A, Lineal B, jeroglífico cretense y
chiprominoico desde 1957. Este índice existe para que toda afirmación de novedad se
compruebe ANTES de escribirse, no después.

Uso:
    python3 nestor_index.py bajar 2015 2026      # descarga los boletines de esos años
    python3 nestor_index.py indexar              # construye nestor_index.json
    python3 nestor_index.py buscar "Linear A" "libation"
    python3 nestor_index.py buscar tema:lineal-a Dikte      # filtra por tema

El índice clasifica cada entrada por FIABILIDAD, que es lo que faltaba:
    revisada   revista con revisión por pares, o volumen de editorial académica
    actas      congreso o volumen colectivo
    tesis      tesis doctoral o de máster
    preprint   repositorio sin revisión (academia.edu, ResearchGate, SSRN, arXiv)
    dudosa     blog, web personal, o sin editorial identificable
"""
import json
import os
import re
import sys
import time
import urllib.request

BASE = 'https://classics.uc.edu/nestor'  # los PDF cuelgan de /images/stories/issues-archived/
UA = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'}

REVISTAS = [
    'kadmos', 'minos', 'smea', 'pasiphae', 'aegean archaeology', 'bsa', 'annual of the british',
    'ajа', 'american journal of archaeology', 'hesperia', 'antiquity', 'journal of archaeological',
    'oxford journal of archaeology', 'cambridge archaeological journal', 'glotta', 'ziva antika',
    'bulletin de correspondance', 'bch', 'revue archéologique', 'gnomon', 'classical review',
    'archäologischer anzeiger', 'jahreshefte', 'studi micenei', 'aegaeum', 'creta antica',
    'ariadne', 'cretan studies', 'journal of hellenic studies', 'jhs', 'zeitschrift für assyriologie',
]
ACTAS = ['colloquium', 'congress', 'proceedings', 'atti', 'actes', 'symposium', 'conference', 'aegaeum']
PREPRINT = ['academia.edu', 'researchgate', 'ssrn', 'arxiv', 'zenodo', 'preprint', 'hal-']
DUDOSA = ['blogspot', 'wordpress', 'wikipedia', 'blog', 'personal website', 'self-published']


def clasificar(texto):
    t = texto.lower()
    if any(k in t for k in DUDOSA):
        return 'dudosa'
    if any(k in t for k in PREPRINT):
        return 'preprint'
    if 'diss' in t or 'thesis' in t or 'tesis' in t:
        return 'tesis'
    if any(k in t for k in REVISTAS):
        return 'revisada'
    if any(k in t for k in ACTAS):
        return 'actas'
    return 'sin clasificar'


def bajar(desde, hasta):
    """Los boletines viven en .../images/stories/issues-archived/AÑO/nedbVV_MMmesAA*.pdf,
    donde VV es el volumen (NESTOR arranca en 1974, así que 2026 es el volumen 53).
    El sufijo del fichero varía (final, corrected, rev...), de modo que se prueban varios."""
    os.makedirs('nestor', exist_ok=True)
    meses = [('01', 'jan'), ('02', 'feb'), ('03', 'mar'), ('04', 'apr'), ('05', 'may'), ('06', 'jun'),
             ('07', 'jul'), ('08', 'aug'), ('09', 'sep'), ('10', 'oct'), ('11', 'nov'), ('12', 'dec')]
    sufijos = ['final', '', 'corrected', 'rev', 'a', 'FINAL', 'Final']
    # el prefijo varía: nedb es el boletín ordinario, necomm otro tipo
    prefijos = ['nedb', 'necomm', 'ne']
    n = 0
    for anio in range(int(desde), int(hasta) + 1):
        # los años antiguos están en un solo PDF anual; los recientes, en mensuales
        anual = 'nestor/%d_anual.pdf' % anio
        if not (os.path.exists(anual) and os.path.getsize(anual) > 20000):
            try:
                req = urllib.request.Request('%s/images/stories/annual_issues/nestor_%d.pdf' % (BASE, anio), headers=UA)
                datos = urllib.request.urlopen(req, timeout=60).read()
                if len(datos) > 20000 and datos[:4] == b'%PDF':
                    open(anual, 'wb').write(datos)
                    n += 1
                    print('  %d  ANUAL   %d KB' % (anio, len(datos) // 1024), flush=True)
                    continue
            except Exception:
                pass
        elif os.path.exists(anual):
            continue
        vol = anio - 1973
        aa = str(anio)[2:]
        for mm, mes in meses:
            destino = 'nestor/%d_%s.pdf' % (anio, mm)
            if os.path.exists(destino) and os.path.getsize(destino) > 20000:
                continue
            hallado = False
            for pre in prefijos:
                for suf in sufijos:
                    url = ('%s/images/stories/issues-archived/%d/%s%d_%s%s%s%s.pdf'
                           % (BASE, anio, pre, vol, mm, mes, aa, suf))
                    try:
                        req = urllib.request.Request(url, headers=UA)
                        datos = urllib.request.urlopen(req, timeout=30).read()
                        if len(datos) > 20000 and datos[:4] == b'%PDF':
                            open(destino, 'wb').write(datos)
                            n += 1
                            hallado = True
                            print('  %d-%s  %-7s %d KB' % (anio, mm, pre, len(datos) // 1024), flush=True)
                            break
                    except Exception:
                        continue
                if hallado:
                    break
            time.sleep(0.2)
    print('\nboletines descargados: %d' % n)
    if n == 0:
        print('ninguno. Comprueba una URL real en el navegador y ajusta el patrón de bajar().')


def indexar():
    """Extrae las entradas bibliográficas de los boletines.

    NESTOR marca cada entrada con un número de referencia §AAAANNNN. Ese marcador es el
    ancla: una entrada va desde su § hasta el siguiente. El texto anterior al primer §
    de cada página es la abreviatura de la serie, que no interesa.
    """
    try:
        import pdfplumber
    except ImportError:
        sys.exit('falta pdfplumber: pip install pdfplumber')
    TEMAS = {
        'lineal-a': ['linear a', 'lineare a', 'minoan script', 'lineal a'],
        'lineal-b': ['linear b', 'lineare b', 'mycenaean greek', 'mycenaean texts', 'pylos tablet', 'knossos tablet'],
        'jeroglifico': ['cretan hieroglyph', 'hieroglyphic script', 'archanes'],
        'chiprominoico': ['cypro-minoan', 'cypriot syllab', 'chypro-minoen'],
        'escritura': ['script', 'writing', 'epigraph', 'inscription', 'sign', 'syllab',
                      'decipher', 'literacy', 'tablet', 'seal', 'sealing', 'nodule', 'roundel'],
        'lengua': ['language', 'lexic', 'onomastic', 'toponym', 'etymolog', 'philolog', 'linguistic'],
    }

    def tema(texto):
        t = texto.lower()
        for nombre, claves in TEMAS.items():
            if any(k in t for k in claves):
                return nombre
        return 'otro'

    entradas = []
    for fichero in sorted(os.listdir('nestor')):
        if not fichero.endswith('.pdf'):
            continue
        try:
            with pdfplumber.open('nestor/' + fichero) as pdf:
                texto = '\n'.join((p.extract_text() or '') for p in pdf.pages)
        except Exception as e:
            print('  %s: no se pudo leer (%s)' % (fichero, str(e)[:40]))
            continue
        antes = len(entradas)
        # cada entrada va de un §AAAANNNN al siguiente
        # el § va al FINAL de la entrada, no al principio: el cuerpo es el trozo ANTERIOR
        trozos = re.split(r'§(\d{8})', texto)
        for k in range(1, len(trozos), 2):
            ref = trozos[k]
            cuerpo = re.sub(r'\s+', ' ', trozos[k - 1]).strip()[-700:]
            # la entrada empieza en el último "Apellido, Nombre ... año" del trozo
            arranques = list(re.finditer(r'[A-ZÀ-Þ][\w\'\-\u00c0-\u024f]+,\s+[A-ZÀ-Þ]', cuerpo))
            if arranques:
                # el que va seguido de un año dentro de los 120 caracteres siguientes
                for m in reversed(arranques):
                    if re.search(r'(19|20)\d\d', cuerpo[m.start():m.start() + 160]):
                        cuerpo = cuerpo[m.start():]
                        break
                else:
                    cuerpo = cuerpo[arranques[-1].start():]
            # la cabecera de página se cuela entre entradas; se retira
            cuerpo = re.sub(r'Nestor \d+\.\d+ \d+ \w+ \d{4}', ' ', cuerpo)
            cuerpo = re.sub(r'\s+', ' ', cuerpo).strip()
            if len(cuerpo) < 40:
                continue
            entradas.append({
                'ref': ref,
                'boletin': fichero[:-4],
                'entrada': cuerpo,
                'fiabilidad': clasificar(cuerpo),
                'tema': tema(cuerpo),
                'anio': ref[:4],
            })
        print('  %-18s %5d entradas' % (fichero, len(entradas) - antes), flush=True)
    vistas = set()
    limpias = []
    for e in entradas:
        if e['ref'] in vistas:
            continue
        vistas.add(e['ref'])
        limpias.append(e)
    json.dump(limpias, open('nestor_index.json', 'w'), ensure_ascii=False, indent=1)
    from collections import Counter
    print('\nentradas únicas: %d' % len(limpias))
    print('por fiabilidad: %s' % dict(Counter(e['fiabilidad'] for e in limpias).most_common()))
    print('por tema:       %s' % dict(Counter(e['tema'] for e in limpias).most_common()))
    print('guardado en nestor_index.json')


def buscar(terminos):
    if not os.path.exists('nestor_index.json'):
        sys.exit('no hay índice: ejecuta primero "indexar"')
    idx = json.load(open('nestor_index.json'))
    tema = None
    if terminos and terminos[0].startswith('tema:'):
        tema = terminos[0][5:]
        terminos = terminos[1:]
    t = [x.lower() for x in terminos]
    hits = [e for e in idx if all(x in e['entrada'].lower() for x in t)
            and (tema is None or e.get('tema') == tema)]
    print('%d entradas contienen %s\n' % (len(hits), ' + '.join(terminos)))
    orden = {'revisada': 0, 'actas': 1, 'tesis': 2, 'sin clasificar': 3, 'preprint': 4, 'dudosa': 5}
    for e in sorted(hits, key=lambda x: (orden.get(x['fiabilidad'], 9), x['entrada'])):
        print('[%-13s] %s' % (e['fiabilidad'], e['entrada'][:150]))
    if not hits:
        print('Nada. Eso NO significa que sea nuevo: significa que NESTOR no lo indexa')
        print('con esos términos. Prueba sinónimos antes de afirmar novedad.')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    orden = sys.argv[1]
    if orden == 'bajar':
        bajar(sys.argv[2] if len(sys.argv) > 2 else 2010, sys.argv[3] if len(sys.argv) > 3 else 2026)
    elif orden == 'indexar':
        indexar()
    elif orden == 'buscar':
        buscar(sys.argv[2:])
    else:
        sys.exit(__doc__)
