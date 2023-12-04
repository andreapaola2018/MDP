import sys
from monte_carlo import monte_carlo_mdp
from MDP_mc import mdp_mc
from value_iteration import * 
from MDP_vi import mdp_vi
from MDP_ql import mdp_ql
from q_learning import QLearning

def runAlgorithm(algorithm): 
    if algorithm == "MC": 
        m = mdp_mc()
        monte_carlo_mdp(m)
    elif algorithm == "VI": 
        m = mdp_vi()
        lambda_value = 0.99 
        VI(m, lambda_value)
    elif algorithm == "QL": 
        m = mdp_ql()
        q = QLearning(m)
        q.train(episodes=1000)
        q.print_results()
        
# user will input algorithm name in command line 
def main():
    algorithm = sys.argv[1]
    runAlgorithm(algorithm) 
    
if __name__ == "__main__":
    main()