"""How much of the variation each level explains, instead of whether a confounder survives.

Yesterday the semantic-field claim was killed by a paired null: shuffle the field label within
scribe, p = 0.117, withdrawn. That answered the question asked but not the one worth asking. The
paired null says *whether* the effect survives the confounder; it does not say how much of the
variation the confounder accounts for, nor how much is left for anything else.

Population genetics has partitioned variance across nested levels since Wright: within an
individual, among individuals of a population, among populations. Our structure is the same shape —
document within scribe within site — and the statistic transfers directly.

    from kuro import Hierarchy
    h = Hierarchy(docs, levels={'site': sites, 'scribe': scribes})
    h.partition(feature=lambda doc: syllable_profile(doc))

What it returns is a share per level, which is what a paired null cannot give.
"""
import math
from collections import defaultdict


def _mean_profile(profiles):
    keys = set().union(*[set(p) for p in profiles]) if profiles else set()
    n = len(profiles) or 1
    return {k: sum(p.get(k, 0.0) for p in profiles) / n for k in keys}


def _sq_dist(p, q):
    keys = set(p) | set(q)
    return sum((p.get(k, 0.0) - q.get(k, 0.0)) ** 2 for k in keys)


class Hierarchy:
    """Two ways in, because two kinds of feature are worth partitioning.

    Scalar: records with named fields, which is the ordinary case.

        Hierarchy(records, levels=['site', 'scribe']).partition('ratio')

    Profile: items with a function that turns each into a distribution, for things like a syllable
    profile where the "value" is a whole vector.

        Hierarchy(items, {'site': sites, 'scribe': scribes}, feature=profile).partition()
    """

    def __init__(self, items, levels, feature=None):
        if feature is None and isinstance(levels, (list, tuple)):
            self._scalar_init(items, levels)
            return
        self._profile_init(items, levels, feature)

    # ---- scalar records ------------------------------------------------------------------------
    def _scalar_init(self, records, level_names):
        self.mode = 'scalar'
        self.records = list(records)
        self.level_names = list(level_names)

    def _scalar_partition(self, field, min_per_group=1):
        recs = [r for r in self.records if field in r]
        n = len(recs)
        groups_at_finest = len({tuple(r.get(l) for l in self.level_names) for r in recs})
        if n < 4 or groups_at_finest < 2:
            return {'note': f'too few records ({n}) or too few groups ({groups_at_finest}) to '
                            f'partition; a partition of this needs at least four records in two '
                            f'groups'}
        vals = [float(r[field]) for r in recs]
        grand = sum(vals) / n
        total = sum((v - grand) ** 2 for v in vals)
        if total == 0:
            return {'note': 'no variation in this field to partition'}
        out, explained, keys = {}, 0.0, []
        for lev in self.level_names:
            keys.append(lev)
            groups = defaultdict(list)
            for r in recs:
                groups[tuple(r.get(k) for k in keys)].append(float(r[field]))
            ss = sum(len(g) * (sum(g) / len(g) - grand) ** 2 for g in groups.values())
            out[lev] = (ss - explained) / total
            explained = ss
        out['residual'] = 1 - explained / total
        out['total_sum_of_squares'] = total
        out['n'] = n
        return out

    # ---- profile items -------------------------------------------------------------------------
    def _profile_init(self, items, levels, feature):
        self.mode = 'profile'
        """items: one entry per document. levels: {name: [label per document]}, outermost first.

        feature: a function from item to a dict of proportions (a profile). Any feature works as
        long as squared distance between profiles is meaningful.
        """
        self.items = list(items)
        self.levels = dict(levels)
        for name, labels in self.levels.items():
            if len(labels) != len(self.items):
                raise ValueError(f'level {name} has {len(labels)} labels for '
                                 f'{len(self.items)} items')
        self.profiles = [feature(x) for x in self.items]
        keep = [i for i, p in enumerate(self.profiles) if p]
        self.keep = keep
        self.profiles = [self.profiles[i] for i in keep]
        self.items = [self.items[i] for i in keep]
        self.levels = {k: [v[i] for i in keep] for k, v in self.levels.items()}

    def partition(self, field=None, **kw):
        """Split the total variation across the nested levels, outermost first."""
        if getattr(self, 'mode', 'profile') == 'scalar':
            if field is None:
                raise ValueError('a scalar partition needs the name of the field to partition')
            return self._scalar_partition(field, **kw)
        return self._profile_partition()

    def _profile_partition(self):
        """Total sum of squares split across the nested levels, outermost first.

        The share at each level is the variation explained by grouping at that level and not
        already explained by a coarser one. What remains is within-group variation.
        """
        if not self.profiles:
            return {'note': 'no usable profiles'}
        grand = _mean_profile(self.profiles)
        total = sum(_sq_dist(p, grand) for p in self.profiles)
        if total == 0:
            return {'note': 'no variation to partition'}

        out, explained, seen_keys = [], 0.0, []
        for name, labels in self.levels.items():
            seen_keys.append(labels)
            groups = defaultdict(list)
            for i, p in enumerate(self.profiles):
                key = tuple(lab[i] for lab in seen_keys)
                groups[key].append(p)
            ss_between = sum(len(g) * _sq_dist(_mean_profile(g), grand) for g in groups.values())
            share = (ss_between - explained) / total
            out.append({'level': name, 'groups': len(groups),
                        'share': share, 'cumulative': ss_between / total})
            explained = ss_between
        out.append({'level': 'within the finest group', 'groups': None,
                    'share': 1 - explained / total, 'cumulative': 1.0})
        return {'total_sum_of_squares': total, 'levels': out,
                'note': ('shares are of total variation and sum to one; a level with a small share '
                         'is not a confounder worth controlling, whatever a paired null says')}

    def report(self):
        r = self.partition()
        if 'levels' not in r:
            return r.get('note', 'nothing to report')
        lines = [f'{len(self.profiles)} items, total sum of squares {r["total_sum_of_squares"]:.4f}',
                 '']
        for lv in r['levels']:
            g = f'{lv["groups"]} groups' if lv['groups'] else ''
            lines.append(f'  {lv["level"]:<26} {100 * lv["share"]:6.1f}%   {g}')
        lines += ['', '  ' + r['note']]
        return '\n'.join(lines)
