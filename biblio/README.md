# Bibliography database

Every substantive claim in `docs/papers/` must point to an entry here, or state explicitly
that no prior art was found and by what search. The purpose is to make prior-art checking a
step in the workflow rather than something discovered afterwards.

## How to use it

`biblio/works.json` holds one record per work. `biblio/claims.json` links each claim in the
papers to the works that bear on it, with a status. `kuro biblio` reports what is unchecked.

Fill `works.json` as sources are obtained. A record with `"held": false` is a source we know
exists and have not read; that is useful information and should stay in the file.

## Fields

    id          short key, e.g. montecchi2009
    authors     list
    year
    title
    venue       journal, volume, pages, or book
    url         where it can be obtained
    held        true if we have the text
    read        true if it has actually been read against our claims
    bears_on    list of claim ids from claims.json
    notes       what it says that matters to us
