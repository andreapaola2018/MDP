from MDP import mdp
import numpy as np 
import matplotlib.pyplot as plt
mdp = mdp() 

discount_rate = 0.99 

def value_iteration(): 
    ##initialize all value estimates to 0 
    V = {s: 0 for s in mdp.states}
    while True: 
        #compute the updated value function for each state 
        new_V = {}
        for s in mdp.states: 
            values = []
            for a in mdp.actions: 
                # print(mdp.transition['RU10p']['P']['RU8a'])
                ##***gets to here and 'a' is sometimes equal to 'any' and some states dont have an action 'any' in rewards list **********  
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
 
        ##if all state values - new state values is lesser than 0.0001 for all states 
        if all(abs(V[s] - new_V[s]) < 0.0001 for s in mdp.states): 
                return new_V
        V = new_V

# ## maximum value function for each state
# V = value_iteration() 
V = value_iteration()
print(V)

##Compute optimal policy 
# policy = {}
# for s in mdp.states: 
#     values = []
#     for a in mdp.actions: 
#         value = mdp.rewards[s][a]
#         for s2 in mdp.states: 
#             value += discount_rate * mdp.transition[s][a][s2] * V[s2]
#         values.append(value)
#     policy[s] = mdp.actions[np.argmax(values)]

# print('optimal policy: ')
# print(policy)

# ##plot 
# policy_values = np.zeros((len(mdp.states), len(mdp.actions)))
# for i,s in enumerate(mdp.states): 
#     for j,a in enumerate(mdp.actions): 
#         policy_values[i,j] = mdp.rewards[s][a] + discount_rate * sum(mdp.transition[s][a][s2] * V[s2] for s2 in mdp.states)


# plt.imshow(policy_values, cmap='Greys')








