# Correr read_literature.py en el Mac

    cd kuro_push_v47              # la carpeta descomprimida
    python3 -m venv .venv && source .venv/bin/activate
    pip install numpy anthropic   # (o pip install -e . anthropic, ya corregido el pyproject)
    PYTHONPATH=. python scripts/read_literature.py --dry          # lista los 48 pasajes, sin llamadas
    export ANTHROPIC_API_KEY=sk-ant-...
    PYTHONPATH=. python scripts/read_literature.py                # 48 llamadas a claude-sonnet-4-6, unos minutos

Resultado: `data/derived/literature_run.json` (proposiciones, informe del lector, eficiencia, supervivientes).
Ese fichero es lo que hay que devolver a la sesión para archivar lo que sobreviva.

# Corrida dirigida por unidad (read_units.py)

    PYTHONPATH=. python scripts/read_units.py --dry     # 133 unidades sin leer, ~447 pasajes, sin llamadas
    PYTHONPATH=. python scripts/read_units.py           # una linea de progreso por pasaje; unos 20-30 min

Resultado: `data/derived/units_run.json`. Devolverlo a la sesion.

# El modelo propone (hypothesize_units.py)

    PYTHONPATH=. python scripts/hypothesize_units.py --dry --limit 5   # muestra las fichas, sin llamadas
    PYTHONPATH=. python scripts/hypothesize_units.py                   # una llamada por unidad (~130), unos 8-10 min
    PYTHONPATH=. python scripts/cycle_units.py data/derived/hypotheses_run.json

Devolver hypotheses_run.json (o el resultado del ciclo, units_cycle.json).

# El modelo PROPONE (propose_units.py), y el ciclo juzga (cycle_proposals.py)

    PYTHONPATH=. python scripts/propose_units.py --dry     # imprime los dosieres, sin llamadas
    caffeinate -i env PYTHONPATH=. python scripts/propose_units.py   # 124 llamadas, una por unidad sin leer, ~8 min

Resultado: `data/derived/proposals_run.json`. Devolverlo a la sesion; el juez (cycle_proposals.py) corre alli.

# NeuroDecipher (Luo, Cao, Barzilay 2019) en el Mac

El codigo es de 2019 (TensorFlow, ortools, cvxopt, cython): usar Python 3.8 en un venv aparte.

    git clone --recursive https://github.com/j-luo93/NeuroDecipher nd && cd nd
    python3.8 -m venv .venv && source .venv/bin/activate
    pip install torch tensorflow ortools cvxopt cython pandas prettytable treelib enlighten pytrie colorlog numpy
    for d in editdistance arglib dev_misc; do (cd $d && pip install .); done; pip install .
    # calibracion: el caso que el articulo resuelve
    python nd/main.py --cfg UgaHebSmallNoSpe
    # los nuestros: copiar data/derived/nd/*.cog del repo kuro a nd/data/ y correr, por candidata,
    python nd/main.py --lost_lang linear_a --known_lang etruscan --cog_path data/linear_a-etruscan.cog --num_cognates 100 --num_rounds 5
    python nd/main.py --lost_lang control  --known_lang etruscan --cog_path data/control-etruscan.cog  --num_cognates 100 --num_rounds 5

Lo que se compara: el coste del emparejamiento (flow cost) que imprime el modelo, minoico real
contra minoico de control, para cada candidata. Sin evaluacion de cognados (no hay verdad).
Si el codigo de 2019 no instala en el Mac, decirlo: no vale la pena pelear mas de media hora.
