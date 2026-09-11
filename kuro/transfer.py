"""The shape of this problem, so that a method from another field can be matched to it.

Every instrument in this package came from outside epigraphy. The hypergeometric co-occurrence
test and the marginal-preserving null come from microbial ecology; the power curve from
experimental design in biology; the capture-artefact control from microscopy. Those are the
results that survived. The ones that failed were mostly borrowed from within the field.

So the scarce resource is not hypotheses: it is **methods from fields with the same structural
problem**. This module states the shape of the problem explicitly, so that the match can be made
deliberately rather than by luck, and records which fields share it and what they solved.

    from kuro import ProblemShape
    ProblemShape.describe()          # what to hand to someone from another field
    ProblemShape.candidates()        # fields with the same shape, and what they have
"""

SHAPE = {
    'units_are': 'discrete tokens (sign-groups, logograms) with no known meaning',
    'documents_are': 'short lists, median one to three units, 1,719 of them',
    'observation': 'presence and quantity of units within documents',
    'vocabulary': '1,006 types, 76% attested once',
    'structure': 'nested: site, scribe, genre, support — documents are not exchangeable',
    'ground_truth': 'absent for the target; available for five calibration corpora',
    'confounders': 'the writing system itself: what is not written cannot be measured',
    'question': 'which units belong to which class, and which co-occur beyond chance',
    'hard_part': 'no verifier — a proposed reading cannot be checked, only made assessable',
}

CANDIDATE_FIELDS = [
    {'field': 'market-basket analysis / association rules',
     'why': 'a Haghia Triada tablet is literally a basket: a short list of items with quantities',
     'shares': ['documents as short item lists', 'co-occurrence is the observation',
                'huge type space, most items rare'],
     'solved': ['support, lift and leverage as measures of interest beside a p-value',
                'the multiple-comparison problem at the scale of millions of candidate rules '
                '(Hamalainen and Webb, arXiv:1709.03904)',
                'the Westfall-Young permutation procedure, which runs the null and the correction '
                'together rather than one after the other (Terada, Tsuda and Sese 2013, PNAS 110)',
                'empirical comparison of which correction controls false positives while still '
                'detecting real rules (arXiv:1110.6652) — the double metric our efficiency module '
                'says it cannot compute',
                'closed and maximal itemsets, which avoid reporting every subset of a finding',
                'the actionable / trivial / inexplicable distinction for mined rules, which names '
                'what our generator mostly produces'],
     'status': 'untried here, and the closest match of the six'},
    {'field': 'rare-species ecology',
     'why': 'the singleton problem: 76% of the vocabulary is attested once, as in a community '
            'sample dominated by rare species',
     'shares': ['singletons dominate', 'sampling effort confounds richness',
                'nestedness across sites'],
     'solved': ['Chao and Jost coverage estimators, already used here for rarefaction',
                'occupancy models that separate absence from non-detection — which is exactly '
                'the absence error this project made twice'],
     'status': 'partly used: coverage yes, occupancy models no'},
    {'field': 'population genetics of small populations',
     'why': 'estimating structure from few observations, with the same anti-conservative bias',
     'shares': ['low power by construction', 'hierarchical structure', 'no ground truth'],
     'solved': ['F-statistics that partition variance across hierarchical levels — the scribe '
                'and site confounders are exactly a hierarchical partition',
                'rarefaction of allelic richness across unequal sample sizes'],
     'status': 'untried; the hierarchical partition is the obvious import'},
    {'field': 'bibliometrics and co-authorship networks',
     'why': 'documents with units, structure by institution, and the same false-positive problem '
            'in co-occurrence',
     'shares': ['bipartite document-unit structure', 'institutional clustering inflates '
                'co-occurrence, as site does here'],
     'solved': ['null models that preserve the bipartite degree sequence',
                'the configuration model for bipartite graphs, which preserves by construction '
                'what our site-paired null has to be told to preserve'],
     'status': 'untried, and the first to bring in: it attacks the 9.2% false-positive rate '
               'measured here at its diagnosed cause, and it is a null, which we already know '
               'how to run'},
    {'field': 'ceramic seriation in archaeology',
     'why': 'ordering assemblages by co-occurrence with no absolute dates',
     'shares': ['co-occurrence is the only signal', 'no external chronology'],
     'solved': ['correspondence analysis and its significance testing',
                'the distinction between a real gradient and one produced by sample size'],
     'status': 'untried; relevant to whether the classes we measure are a gradient'},
    {'field': 'cryptanalysis of historical ciphers',
     'why': 'the Descrypt project builds a database precisely because data is scarce',
     'shares': ['scarce data', 'transcription errors propagate into analysis'],
     'differs': ['the plaintext language is known and the answer is verifiable — which is the '
                 'whole difference, and why their methods do not transfer directly'],
     'solved': ['error models for transcription, which this project has not built'],
     'status': 'a sixth calibration corpus rather than a source of methods'},
]


class ProblemShape:
    @staticmethod
    def describe():
        lines = ['The problem, stated so that someone outside epigraphy can recognise it:', '']
        for k, v in SHAPE.items():
            lines.append(f'  {k.replace("_", " "):<16} {v}')
        return '\n'.join(lines)

    @staticmethod
    def candidates(status=None):
        out = [c for c in CANDIDATE_FIELDS if status is None or status in c['status']]
        lines = []
        for c in out:
            lines.append(f'{c["field"]}  [{c["status"]}]')
            lines.append(f'  why      : {c["why"]}')
            lines.append('  shares   : ' + '; '.join(c['shares']))
            if c.get('differs'):
                lines.append('  differs  : ' + '; '.join(c['differs']))
            lines.append('  has      : ' + '; '.join(c['solved']))
            lines.append('')
        return '\n'.join(lines)

    @staticmethod
    def untried():
        return [c['field'] for c in CANDIDATE_FIELDS if 'untried' in c['status']]
