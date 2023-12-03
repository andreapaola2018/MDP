from MDP_mc import mdp_mc

# first-visit monte carlo method for traversing the MDP
def monte_carlo_mdp(model: mdp_mc, numEpisodes=50, alpha=0.1):
    # keeps track of the state value estimates for each state
    stateValueEstimate = {}
    # keeps track of the total number of visits to each state, in order to be used for first-visits to states
    numVisitsToState = {}
    # keeps track of the rewards received for each visit to each state
    rewardsForState = {}
    # initialize each of the above three dictionaries with each state in the model
    for state in model.statesAndActions:
        numVisitsToState[state] = 0 # each state has been visited 0 times
        rewardsForState[state] = 0 # each state currently has 0 reward
        stateValueEstimate[state] = 0 # each state starts with a value estimate of 0
    
    # episode simulation
    for episodeNum in range(numEpisodes):
        visitedStates = [] # keep track of all visited states in the episode
        rewards = [] # keep track of the rewards for each visited state in the episode
        currState = mdp_mc.initialState # starting state
        visitedStates.append(currState)
    
        print("Simulating episode: ", episodeNum+1)
        print("Sequence: ", currState, end="")
        terminalState = False
        
        # randomly generate actions throughout the simulation until terminal state is reached
        while not terminalState:
            # select an action at random from available actions
            action = model.chooseActionFromState(currState)
            # take the selected random action from the current state
            newState, reward = model.takeAction(currState, action)
            rewards.append(reward) # keep track of the reward from taking that action
            print("->(", action, ", ", reward, ")->", newState, end="", sep="")
            
            # if it is not a terminal state, move on to the next state
            if not model.isTerminalState(newState):
                visitedStates.append(newState)
                currState = newState
            else: # if terminal state, done
                terminalState = True
        
        numVisited = len(visitedStates) # how many states did we visit?
        ret = 0 # used to calculate the total return for the episode
        sumOfRewards = 0 # used to calculate the sum of the raw rewards for the episode, without using the learning rate
        
        # traverse backwards through all visited states to calculate the reward
        # using first-visit monte carlo method
        for i in range(numVisited-1, -1, -1):
            state = visitedStates[i]
            reward = rewards[i]
            sumOfRewards += reward

            ret = alpha * ret + reward
            
            if state not in visitedStates[0:i]: # if the state has not been visited yet, first visit
                numVisitsToState[state] += 1
                rewardsForState[state] += ret
        
        print("\nSum of Rewards for Episode ", episodeNum+1, ": ", sumOfRewards)
        print("Average reward for episode ", episodeNum+1, ": ", sumOfRewards/numVisited, "\n", sep="")
      
    # once done with episode simulation, calculate the state value estimate for each state  
    for state in model.statesAndActions:
        if numVisitsToState[state] != 0:
            stateValueEstimate[state] = rewardsForState[state]/numVisitsToState[state]
        
    # printing purposes
    print("Simulation Finished. Values of all the States:")
    for state in stateValueEstimate:
        print(state, ": ", stateValueEstimate[state], sep="")
        
    return stateValueEstimate