
# Problem: Student and the decisions one must make to both have a 
# good and remain in good academic standing 
# States: R, T, D, U, 8p
# Actions: P, R, S, any 
# Reward: Dictionary mapping with each state action pair 

import numpy as np 
import matplotlib

states = ['RU8p', 'RU10p','RU8a','RU10a',
          'TU10p', 'TU10a',
          'TD10a', 
          'RD10p', 'RD8a', 'RD10a',
          'ClassBegins']
actions = ['P', 'R', 'S', 'any']
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
              'TU10p': {'P': {'RU10a': 1.0}, 'R': {'RU8a': 1.0}}
}