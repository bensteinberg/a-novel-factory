import json


class Corpora:
    """ 
    This class is a mechanism for loading subsets of data from a
    a copy of https://github.com/dariusk/corpora stored locally
    as a git submodule.
    """
    def __init__(self):
        with open('corpora/data/humans/atus_activities.json') as f:
            self.activities = [
                example.replace('hh', 'household') for examples in [
                    c['examples']
                    for c in json.load(f)['categories']
                    if 'examples' in c
                ] for example in examples
                if example.split()[0].endswith('ing')
            ]
