"""The Anatolian corpora of eDiAna as comparanda for the Minoan vowel profile.

Finkelberg (1990, 2001) argues from the near-absence of the o-series in Linear A that Minoan
had a four-vowel system, and concludes that Minoan is Anatolian with Lycian its descendant.
That argument can only be tested against languages written in a script that distinguishes o,
which excludes the seven cuneiform candidates. Lycian, Lycian B and Lydian have alphabets of
their own, so the test applies to them and to no other member of her comparison.

The eDiAna corpora (LMU Munich, CC BY-SA 4.0) are returned by its API as one JSON object per
text, mapping the text label to a list of word records.
"""
import glob
import json
import os
import re
from collections import Counter

VOWELS = 'aeiou'


def load_text(path):
    """One eDiAna JSON file: returns (label, [word strings])."""
    with open(path, encoding='utf-8') as fh:
        raw = fh.read().strip()
    if not raw or raw in ('[]', '{}'):
        return None, []
    data = json.loads(raw)
    if isinstance(data, list):
        return None, []
    label = next(iter(data))
    words = []
    for rec in data[label]:
        if not isinstance(rec, dict):
            continue
        # the transliterated line is in 'sentence'; 'word' holds the line number
        text = rec.get('sentence') or ''
        if text.startswith('(') or not text or text == 'None':
            continue
        words.extend(text.split())
    return label, words


def load_corpus(directory, language):
    """Every text of one language, as {label: [words]}."""
    out = {}
    for path in sorted(glob.glob(os.path.join(directory, f'{language}_*.json'))):
        label, words = load_text(path)
        if label:
            out[label] = words
    return out


def is_word(token):
    """Editorial matter, line markers and translations are not words of the language."""
    if not token or len(token) > 40:
        return False
    if re.search(r'[A-Z]{2,}|:|\d', token):
        return False
    return bool(re.search(r'[a-zñẽãĩõũâêîôûáéíóúα-ω]', token.lower()))


def vowel_profile(words):
    """The share of each vowel among all vowel occurrences, and the count."""
    counts = Counter()
    for w in words:
        if not is_word(w):
            continue
        for ch in w.lower():
            base = {'ã': 'a', 'ẽ': 'e', 'ĩ': 'i', 'õ': 'o', 'ũ': 'u',
                    'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
                    # Pisidian and Sidetic are written in the Greek alphabet
                    'α': 'a', 'ε': 'e', 'η': 'e', 'ι': 'i', 'ο': 'o',
                    'ω': 'o', 'υ': 'u', 'ᾱ': 'a', 'ῑ': 'i'}.get(ch, ch)
            if base in VOWELS:
                counts[base] += 1
    total = sum(counts.values())
    if not total:
        return None, 0
    return {v: counts[v] / total for v in VOWELS}, total


def distance(profile_a, profile_b):
    """Total variation between two vowel profiles: 0 identical, 1 disjoint."""
    return sum(abs(profile_a[v] - profile_b[v]) for v in VOWELS) / 2
