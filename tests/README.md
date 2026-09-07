Run with `pytest -q` from the repository root. All tests use synthetic data with a known answer:
a planted register difference, a planted prefix, planted mutually exclusive blocks, a vocabulary that
depends on the hand and not on the support, and a tablet whose total adds up. They check that each
instrument sees what is there and that the nulls preserve what they must (margins, lengths, strata).
