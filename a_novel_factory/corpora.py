import json
import random


class Corpora:
    """
    This class is a mechanism for loading subsets of data from a
    a copy of https://github.com/dariusk/corpora stored locally
    as a git submodule.
    """
    def __init__(self, path='corpora/data'):
        # combine lists of lists of American Time Use Survey activities
        with open(f'{path}/humans/atus_activities.json') as f:
            self.activities = [
                example.replace('hh', 'household') for examples in [
                    c['examples']
                    for c in json.load(f)['categories']
                    if 'examples' in c
                ] for example in examples
                if example.split()[0].endswith('ing')
            ]

        # pick a province, then get a subset of municipalities
        with open(f'{path}/geography/canadian_municipalities.json') as f:
            municipalities = json.load(f)['municipalities']
        province = random.choice(
            sorted(list(set([m['province'] for m in municipalities])))
        )
        places = [
            m['name'] for m in municipalities if m['province'] == province
        ]
        self.places = random.sample(places, k=random.randint(1, len(places)))

        # get all the objects, except those that are plural
        with open(f'{path}/objects/objects.json') as f:
            self.objects = [o for o
                            in json.load(f)['objects']
                            if o[-1] != 's' or ' ' in o]

        # get most of the "adjectives"; a number of these are
        # not really adjectives...
        with open(f'{path}/words/adjs.json') as f:
            self.adjectives = [a for a
                               in json.load(f)['adjs']
                               if not a[0].isupper()]
