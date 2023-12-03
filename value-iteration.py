from MDP import mdp
import numpy as np 
import matplotlib.pyplot as plt
mdp = mdp() 

discount_rate = 0.99 

def value_iteration(): 
    ##initialize all value estimates to 0 
    V = {s: 0 for s in mdp.states}
    state_iterations = {s: 0 for s in mdp.states}
    while True: 
        #compute the updated value function for each state 
        new_V = {}
        for s in mdp.states: 
            values = []
            for a in mdp.actions: 
                value = mdp.rewards[s].get(a, 0)  # Default to 0 if action not available in state     
                for s2 in mdp.states: 
                    ## transition[s][a][s2] is the probability of transitioning to state s2 
                    ## V[s2] is the current value estimate of s2
                    if s in mdp.states and a in mdp.actions and s2 in mdp.states: 
                         if a in mdp.transition[s] and s2 in mdp.transition[s][a]: 
                            print("\nPrevious Value: ", value)
                            value += discount_rate * mdp.transition[s][a][s2] * V[s2]
                            print("New Value: ", value)

                         else: ## handling case where s2 in not in transition probabilities
                            value+= discount_rate * 0 * V[s2]
                    else: 
                        ##invalid state or action 
                        value+= discount_rate * 0 * V[s2]      
                values.append(value)
            
            # Find the index of the action that maximizes the value
            max_value_index = values.index(max(values))
            selected_action = mdp.actions[max_value_index]
            
            # Print out the selected action for the current state
            print(f"State: {s}, Selected Action: {selected_action}")
            new_V[s] = max(values)
            state_iterations[s] += 1 ##increment iteration counter for the current state 

 
        ##if all state values - new state values is lesser than 0.0001 for all states 
        if all(abs(V[s] - new_V[s]) < 0.0001 for s in mdp.states): 
                return new_V, state_iterations
        V = new_V

# ## maximum value function for each state
# V = value_iteration() 
V, state_iterations = value_iteration()
print("\nFinal Values for Each State: ")
print(V)
print("\nNumber of Iterations For Each State:")
for s, iterations in state_iterations.items(): 
    print(f"{s}: {iterations}")

policy = {}

for s in mdp.states: 
    values = []
    for a in mdp.actions: 
        value = 0
        if s in mdp.rewards and a in mdp.rewards[s]:
            # If the action is defined in rewards for the state
            value += mdp.rewards[s][a]
        # value = mdp.rewards[s][a] # Default to 0 if action not available in state
        for s2 in mdp.states: 
            if s in mdp.states and a in mdp.actions and s2 in mdp.states: 
                if a in mdp.transition[s] and s2 in mdp.transition[s][a]: 
                    value += discount_rate * mdp.transition[s][a][s2] * V[s2]
        values.append(value)

    if s == 'TU10a' or s == 'RU10a': 
       policy[s] = mdp.actions[3]
    else: 
        policy[s] = mdp.actions[np.argmax(values)] ##maximum of actions 

# Print the final optimal policy
print('\nFinal Optimal Policy:')
print(policy)