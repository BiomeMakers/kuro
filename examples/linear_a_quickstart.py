"""Quickstart on Linear A (LinearA Explorer JSON). Adjust the path."""
import random; random.seed(1)
from kuro import load_lineara, profile_distance, affix_pairs, metacommunity, confounder_jaccard, totals_check, hapax_by_length
docs = load_lineara('lineara.xyz-master/items_analysis/inscriptions.json')
tab = [d for d in docs if d.support == 'Tablet' and d.site == 'Haghia Triada']
cult = [d for d in docs if d.site in ('Iouktas', 'Petsophas', 'Syme', 'Kophinas', 'Psychro', 'Vrysinas')]
print('registro (HT tablillas vs santuarios):', profile_distance(tab, cult, size=200))
vocab = sorted(set(w for d in docs for w in d.words() if '-' in w))
print('prefijo KA-:', {k: v for k, v in affix_pairs(vocab, 'ka', 'prefix').items() if k != 'pairs'})
print('sufijo -JA:', {k: v for k, v in affix_pairs(vocab, 'ja', 'suffix').items() if k != 'pairs'})
print('metacomunidad:', {k: (v if k == 'shape' else len(v)) for k, v in metacommunity(tab).items()})
typ = lambda d: 'personal' if any(t.startswith('VIR') for t in d.tokens) else ('produccion' if any(t in ('GRA', 'OLIV', 'OLE+U') for t in d.tokens) else 'otro')
print('mano vs tipo:', confounder_jaccard([d for d in tab if d.hand], lambda d: d.hand, typ, n_null=100))
print('KU-RO en HT 117a:', totals_check(next(d for d in docs if d.id == 'HT117a')))
print('hapax por longitud:', hapax_by_length(tab))
