
# Problem: Student and the decisions one must make to both have a 
# good and remain in good academic standing 
# States: R, T, D, U, 8p
# Actions: P, R, S, any 
# Reward: Dictionary mapping with each state action pair 

import numpy as np 
# import matplotlib

class mdp: 

    states = ['RU8p', 'RU10p','RU8a','RU10a',
            'TU10p', 'TU10a',
            'TD10a', 
            'RD10p', 'RD8a', 'RD10a',
            'ClassBegins']

    actions = ['P', 'R', 'S', 'any', 'P1','P2']
    rewards = {'RU8p': {'P': 2, 'R': 0, 'S': -1},
            'RU10p': {'P1': 2, 'P2': 2, 'R': 0, 'S': -1},
            'RU8a': {'P': 2, 'R': 0, 'S': -1},
            'RU10a': {'any': 0},
            'TU10p': {'P': 2, 'R': 0},
            'TU10a': {'any', -1},
            'RD10p': {'R': 0, 'P1': 2, 'P2': 2}, 
            'RD8a': {'R': 0, 'P': 2},
            'RD10a': {'any': 4}, 
            'TD10a': {'any': 3}
    }
    transition = {'RU8p': {'P': {'TU10p': 1.0 }, 'R': {'RU10p': 1.0},'S': {'RD10p': 1.0}},
                'TU10p': {'P': {'RU10a': 1.0}, 'R': {'RU8a': 1.0}},
                'RU10p': {'R':{'RU8a': 1.0}, 'P1':{'RU8a': .5}, 'P2': {'RU10a': .5},'S': {'RD8a': 1.0}},
                'RD10p': {'R': {'RD8a': 1.0}, 'P1': {'RD8a': .5}, 'P2': {'RD10a': .5}}, 
                'RU8a': {'P': {'TU10a': 1.0}, 'R': {'RU10a': 1.0}, 'S': {'RD10a': 1.0}},
                'RD8a': {'R': {'RD10a': 1.0}, 'P': {'TD10a': 1.0}}, 
                'TU10a': {'any': {'ClassBegins': 1.0}},
                'RU10a': {'any': {'ClassBegins': 1.0}},
                'RD10a': {'any': {'ClassBegins': 1.0}},
                'TD10a': {'any': {'ClassBegins': 1.0}}

    }