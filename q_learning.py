from MDP_ql import mdp_ql
import numpy as np

class QLearning: 
    def __init__(self, mdp: mdp_ql, alpha=0.2, gamma=0.99, epsilon=0.001): 
        self.mdp = mdp
        self.alpha = alpha
        self.gamma = gamma ##discount rate
        self.epsilon = epsilon
        ##initialize Q-values for each state, action pair to 0 
        self.q_values = {state: {action: 0.0 for action in actions} for state, actions in mdp.statesAndActions.items()}

    # randomly choose action
    def choose_action(self, state):
        return np.random.choice(self.mdp.statesAndActions[state])

    def update_q_value(self, state, action, reward, next_state):
        old_q_value = self.q_values[state][action]

        #if next state has no available actions , set max q value to 0
        if not self.q_values[next_state]: 
            max_next_q_value = 0.0

        #get max value 
        else: 
            max_next_q_value = max(self.q_values[next_state].values())
        new_q_value = (1 - self.alpha) * old_q_value + self.alpha * (reward + self.gamma * max_next_q_value)
        self.q_values[state][action] = new_q_value

        print(f"State: {state}, Action: {action}")
        print(f"Previous Q Value: {old_q_value}")
        print(f"Immediate Reward: {reward}")
        print(f"Next State: {next_state}")
        print(f"New Q Value: {new_q_value}\n")

        return abs(new_q_value - old_q_value)
    
    def train(self, episodes): 
        for episode in range(1, episodes+1): 
            state = self.mdp.initialState
            total_q_value_change = 0

            while not self.mdp.isTerminalState(state): 
                action = self.choose_action(state)
                next_state, reward = self.mdp.takeAction(state, action)
                q_value_change = self.update_q_value(state, action, reward, next_state)
                total_q_value_change = max(total_q_value_change, q_value_change)
                state = next_state
            print(f"Episode {episode} - Total Q Value Change: {total_q_value_change}")
            self.alpha *= 0.995  # Decrease alpha after each episode

            if total_q_value_change < self.epsilon:
                print(f"\nConverged after {episode} episodes!")
                break
    
    def print_results(self): 
        print("\nFinal Q Values:")
        for state, actions in self.q_values.items():
            print(f"State: {state}, Q Values: {actions}")
        
        optimal_policy = {state: max(actions, key=actions.get) for state, actions in self.q_values.items() if actions}
        print("\nOptimal Policy:")
        print(optimal_policy)


mdp_qlearning = mdp_ql()
q_learning_agent = QLearning(mdp_qlearning)
q_learning_agent.train(episodes=1000)
q_learning_agent.print_results()