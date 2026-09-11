"""One format for every candidate language, so that they can be compared at all.

Two attempts on 10 September 2026 to compare Minoan with its candidate relatives failed at the same
place: the corpora are not written the same way. Ugaritic has no vowels, Hittite has cuneiform
closed syllables, Etruscan and Greek are alphabetic, Linear A and B are CV syllabaries read with
Greek values. Any distance between them measures the writing system before it measures the language.

This module reduces every corpus to a **declared common skeleton** so that structural and
morphological features can be compared. It does not pretend to recover phonology: the skeleton
throws information away on purpose, and what it keeps is what every transcription preserves.

Two skeletons, each with its declared loss:

  consonantal   each word -> its consonant sequence, vowels dropped, with a declared mapping
                loses: vowels, length, tone. keeps: root structure, which Semitic and much of
                the Near East organises words around. Ugaritic is already this.

  syllabic      each word -> CV syllables by a fixed rule (a consonant takes the vowel that
                follows it; clusters split; a final consonant becomes its own unit)
                loses: cluster structure. keeps: syllable count, first and last syllable, which
                is what the affix and formula measures use. Linear A is already this.

    from kuro import Normalizer
    N = Normalizer('consonantal')
    N.words(etruscan_words)        # -> list of skeletons
    N.report(corpora)              # how much each corpus lost, so the loss is on record
"""
import re
from collections import Counter

# What counts as a vowel across the transcriptions we hold. Declared, not guessed.
VOWELS = set('aeiouāēīōūáéíóúàèìòùâêîôûıɨəə̂yy̑')
# Digraphs and marks that stand for one consonant in the transcriptions we hold.
CONSONANT_MAP = {
    'ḫ': 'x', 'h': 'x', 'ḥ': 'x', 'ḳ': 'q', 'ṣ': 's', 'š': 's', 'ś': 's', 'ṭ': 't', 'ṯ': 't',
    'ḏ': 'd', 'ẓ': 'z', 'ġ': 'g', 'θ': 't', 'φ': 'p', 'χ': 'k', 'ʾ': "'", 'ʿ': "'", '<': "'",
    '>': "'", 'ǵ': 'g', 'ḷ': 'l', 'ṛ': 'r',
}
DROP = set('-.,:;()[]{}?!/\\|•·₂₃₄ʼ’"' + "0123456789")


def _clean(w):
    w = w.lower()
    return ''.join(CONSONANT_MAP.get(ch, ch) for ch in w if ch not in DROP)


class Normalizer:
    def __init__(self, skeleton='consonantal'):
        if skeleton not in ('consonantal', 'syllabic'):
            raise ValueError('skeleton must be consonantal or syllabic')
        self.skeleton = skeleton
        self.loss = {}

    # ---- consonantal --------------------------------------------------------------------------
    def _consonantal(self, w):
        w = _clean(w)
        # syllabified transcriptions (Linear A/B) use hyphens; a CV syllable's consonant is its first char
        cons = [ch for ch in w if ch not in VOWELS and ch.isalpha() or ch == "'"]
        return ''.join(cons)

    # ---- syllabic -----------------------------------------------------------------------------
    def _syllabic(self, w):
        w = _clean(w)
        out, i = [], 0
        while i < len(w):
            ch = w[i]
            if ch in VOWELS:
                out.append(ch); i += 1; continue
            # consonant: take the vowel that follows, if any
            if i + 1 < len(w) and w[i + 1] in VOWELS:
                out.append(ch + w[i + 1]); i += 2
            else:
                out.append(ch); i += 1
        return '-'.join(out)

    def word(self, w):
        return self._consonantal(w) if self.skeleton == 'consonantal' else self._syllabic(w)

    def words(self, ws):
        return [self.word(w) for w in ws if w and w.strip()]

    def report(self, corpora):
        """How much each corpus lost in the reduction: a declared loss, not a hidden one."""
        lines = [f'skeleton: {self.skeleton}', '',
                 f'{"corpus":<14}{"words":>8}{"types before":>14}{"types after":>13}{"collapsed":>11}']
        for name, ws in corpora.items():
            ws = [w for w in ws if w and w.strip()]
            before = len(set(ws))
            sk = self.words(ws)
            after = len(set(sk))
            lines.append(f'{name:<14}{len(ws):>8}{before:>14}{after:>13}{100 * (1 - after / before):>10.1f}%')
            self.loss[name] = 1 - after / before
        lines += ['', 'collapsed = share of distinct words that became indistinguishable; the '
                      'skeleton is only comparable across corpora where this loss is similar']
        return '\n'.join(lines)
