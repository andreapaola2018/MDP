import sys
from monte_carlo import monte_carlo_mdp
from MDP_mc import mdp_mc
from value_iteration import * 
from MDP import mdp
def runAlgorithm(algorithm): 
    if algorithm == "MC": 
        m = mdp_mc()
        monte_carlo_mdp(m)
    elif algorithm == "VI": 
        m = mdp()
        lambda_value = 0.99 
        VI(m, lambda_value)
    elif algorithm == "QL": 
        pass

# user will input algorithm name in command line 
def main():
    algorithm = sys.argv[1]
    runAlgorithm(algorithm) 
    
if __name__ == "__main__":
    main()