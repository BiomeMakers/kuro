"""How much information a corpus contains about its own decipherment.

Every proposal to read an undeciphered script argues about whether the thing can be done.
The argument is usually qualitative. It need not be: a decipherment is an assignment of
values to signs, its cost in bits follows from the size of the sign inventory, and what the
corpus can supply toward that cost follows from how often a candidate reading succeeds by
chance. The difference is the deficit, and it is a property of the corpus, not of the
method or of the investigator.

    cost      = free signs x log2(possible values) + log2(candidate languages)
    supply    = independent units x -log2(chance match rate)
    deficit   = cost - supply
    anchor    = log2(possible values) bits removed per sign fixed from outside

The estimate is deliberately generous to the corpus: it counts every unit as independent
evidence when units share signs, and it ignores that a match must also be contextually
right. A corpus that shows a deficit under these assumptions shows one under any.
"""
import math


class Corpus:
    """The four quantities any undeciphered script can report about itself."""

    def __init__(self, name, signs, anchored, units, match_rate,
                 values=None, languages=1):
        if not 0 < match_rate < 1:
            raise ValueError('match_rate must lie strictly between 0 and 1')
        if anchored > signs:
            raise ValueError('cannot anchor more signs than the script has')
        self.name = name
        self.signs = signs
        self.anchored = anchored
        self.units = units
        self.match_rate = match_rate
        self.values = values if values is not None else signs
        self.languages = languages

    @property
    def free(self):
        return self.signs - self.anchored

    @property
    def bits_per_sign(self):
        return math.log2(self.values)

    @property
    def cost(self):
        """Bits needed to specify one assignment, plus the choice of language."""
        return self.free * self.bits_per_sign + math.log2(self.languages)

    @property
    def bits_per_unit(self):
        """Information carried by one unit matching, given how often chance matches."""
        return -math.log2(self.match_rate)

    @property
    def supply(self):
        return self.units * self.bits_per_unit

    @property
    def deficit(self):
        return self.cost - self.supply

    @property
    def decipherable(self):
        return self.deficit <= 0

    def anchors_needed(self):
        """How many further signs must be fixed from outside to close the deficit."""
        if self.deficit <= 0:
            return 0
        return math.ceil(self.deficit / self.bits_per_sign)

    def units_needed(self):
        """How many further units would close it, if more text were found instead."""
        if self.deficit <= 0:
            return 0
        return math.ceil(self.deficit / self.bits_per_unit)

    def report(self):
        return {
            'name': self.name,
            'free_signs': self.free,
            'cost_bits': round(self.cost),
            'supply_bits': round(self.supply),
            'deficit_bits': round(self.deficit),
            'decipherable': self.decipherable,
            'anchors_needed': self.anchors_needed(),
            'units_needed': self.units_needed(),
        }
