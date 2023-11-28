import numpy as np

state = {
    0 : "Burger",
    1 : "Pizza",
    2 : "Hotdog"
}

# Transition matrix
transitions = np.array([[0.2,0.6,0.2],[0.3,0,0.7],[0.5,0,0.5]])

# # Simulate a random walk
# n = 50 # 50 episodes
# start_state = 0
# print(state[start_state], "--->", end=" ")
# prev_state = start_state

# while n-1:
#     curr_state = np.random.choice([0,1,2], p=transitions[prev_state])
#     print(state[curr_state], "--->", end=" ")
#     prev_state = curr_state
#     n-=1
# print("stop")

# steps = 50
# start_state = 0
# pi = np.array([0,0,0])
# pi[start_state] = 1
# prev_state = start_state

# i = 0
# while i<steps:
#     curr_state = np.random.choice([0,1,2], p=transitions[prev_state])
#     pi[curr_state] += 1
#     # print(state[curr_state], "--->", end=" ")
#     prev_state = curr_state
#     i+=1
# print("π = ", pi/steps)

monte_carlo_mdp(mdp, num_episodes=50, alpha=0.1):
    