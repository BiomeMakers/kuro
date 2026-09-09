"""kuro: null models, calibration and confounder tests for small epigraphic corpora.

Corpus = list of Document(id, site, support, date, hand, tokens) where tokens are sign-groups,
logograms and quantities in reading order. Every test returns an observed statistic, a null
distribution summary and a p-value. Nothing here reads a language; everything here says what a
corpus can and cannot support.
"""
from .corpus import Document, load_lineara, load_cdli_atf, load_csv_texts
from .nulls import shuffle_labels, shuffle_within_strata, curveball, shuffle_syllables
from .tests import (profile_distance, affix_pairs, family_positions, metacommunity,
                    monopolies, confounder_jaccard, totals_check, form_screen, hapax_by_length,
                    capture_artifact, group_cohesion, factor_effects)
from .mine import doubts
from .report import Corpus, FRACTION_VALUES, power_report, POWER_THRESHOLDS
from .provenance import Fact, file_hash
from .evidence import Value, computed, cited, illustrative, corpus_hash, COMPUTED, CITED, ILLUSTRATIVE
__version__ = "0.1.0"
