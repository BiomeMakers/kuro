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
from .reference import Reference
from .dictionary import Dictionary, Entry
from .hypothesis import Hypothesis
from .constraints import Constraints, Rule
from .orders import Orders
from .bipartite import BipartiteNull
from .hierarchy import Hierarchy
from .westfall import WestfallYoung
from .predictive import PredictiveTest
from .reader import Reader, Proposition
from .propose import Proposer
from .normalize import Normalizer
from .hierarchy import Hierarchy
from .westfall import WestfallYoung
from .predictive import PredictiveTest
from .reader import Reader, Proposition
from .propose import Proposer
from .normalize import Normalizer
from .iterate import Iteration, CircularSupport
from .errorrate import ErrorRate
from .lessons import Lessons
from .generate import Generator, Candidate
from .transfer import ProblemShape
from .efficiency import Efficiency
from .generate import Generator
from .evidence import Value, computed, cited, illustrative, corpus_hash, COMPUTED, CITED, ILLUSTRATIVE
__version__ = "0.1.0"
