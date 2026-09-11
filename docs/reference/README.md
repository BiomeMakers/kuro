# docs/reference/ — the works to look a word up in, before measuring it

The `kuro.Reference` class indexes plain-text extractions of the reference works and lets you ask,
in one line, what the literature already says about a sign-group:

```python
from kuro import Reference
ref = Reference('docs/reference')
print(ref.lookup('KU-NI-SU'))
print(ref.unread(['KU-NI-SU', 'SA-RU', 'KI-RE-TA-NA']))
```

**Why it exists.** In one week this project measured something, concluded something, and then found
the conclusion already published — six times. Twice it was in Younger's Lexicon, which catalogues
the corpus word by word and is freely available. The cost each time was an afternoon. This is the
cure, and it takes a second.

**The rule that follows from it: look the word up before you measure it, not after.**

## What goes in this folder

Plain-text extractions, one file per work, named `author_shorttitle_year.txt`. Make them yourself
from PDFs you obtain; **nothing here is redistributed with this package**, and the extractions are
listed in `.gitignore` for the public deposit.

| file | work | where to get it |
|---|---|---|
| `younger_lexicon_2024.txt` | Younger, J. G., *Linear A Lexicon*, updated 26 May 2024 | academia.edu/120182223 |
| `younger_ht_commentary_2024.txt` | Younger, J. G., *Linear A Texts and Inscriptions in phonetic transcription and Commentary*, 8 April 2024 | academia.edu/117949876 |
| `salgarella_petrakis_2025_worlds.txt` | Salgarella and Petrakis (eds), *The Wor(l)ds of Linear A*, AURA Suppl. 15, 2025 | open access, AURA |

Worth adding when obtained: van Soesbergen's chapter 13 (onomastics, pp. 503-955), Davis 2014 on
the stone vessels, Palmer 1995 on commodities, Schoep 2002.

## Making an extraction

```
pdftotext -layout work.pdf docs/reference/author_shorttitle_year.txt
```

If the PDF is a scan with no text layer, OCR it first. Two of the works used in this project
(Duhoux on morphosyntax, Melena 1974) are scans and could not be read at all until they were OCR'd.
