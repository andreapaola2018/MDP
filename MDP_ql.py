import numpy as np 

class mdp_ql: 
    state_count = 11
    action_count = 4
    initialState = 'RU8p'
    terminalState = 'ClassBegins'
    statesAndActions = {'RU8p': ['P', 'R', 'S'],
                'TU10p': ['P', 'R'],
                'RU10p': ['R', 'P', 'S'],
                'RD10p': ['R', 'P'], 
                'RU8a': ['P', 'R', 'S'],
                'RD8a': ['R', 'P'], 
                'TU10a': ['any'],
                'RU10a': ['any'],
                'RD10a': ['any'],
                'TD10a': ['any'],
                'ClassBegins': [],
    }
    transitions = {'RU8p': {'P': ['TU10p', 2], 'R': ['RU10p', 0],'S': ['RD10p', -1]},
                'TU10p': {'P': ['RU10a', 2], 'R': ['RU8a', 0]},
                'RU10p': {'R':['RU8a', 0], 'P': ['RU8a', 'RU10a', 2], 'S': ['RD8a', -1]},
                'RD10p': {'R': ['RD8a', 0], 'P': ['RD8a', 'RD10a', 2]}, 
                'RU8a': {'P': ['TU10a', 2], 'R': ['RU10a', 0], 'S': ['RD10a', -1]},
                'RD8a': {'R': ['RD10a', 0], 'P': ['TD10a', 2]}, 
                'TU10a': {'any': ['ClassBegins', -1]},
                'RU10a': {'any': ['ClassBegins', 0]},
                'RD10a': {'any': ['ClassBegins', 4]},
                'TD10a': {'any': ['ClassBegins', 3]}
    }
    
    # returns an action at random from the given state
    def chooseActionFromState(self, state: str) -> str:
        return np.random.choice(self.statesAndActions[state])

    # given a state, takes the action specified
    def takeAction(self, state: str, action: str) -> (str, int):
        possibleTransitions = self.transitions[state][action]
        if len(possibleTransitions) == 2:
            return possibleTransitions[0], possibleTransitions[1]
        ranState = np.random.randint(0,2)
        return possibleTransitions[ranState], possibleTransitions[2]
        

    # return true iff the given state is a terminal state
    def isTerminalState(self, state: str) -> bool:
        return state == self.terminalState
    