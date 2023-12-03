import sys
from value_iteration import * 
from MDP import mdp
def runAlgorithm(algorithm): 
    if algorithm == "MC": 
        print("MC")
        pass
    elif algorithm == "VI": 
        m = mdp()
        lambda_value = 0.99 
        VI(m, lambda_value)
    elif algorithm == "QL": 
        pass

##user will input algorithm name in command line 
def main():
    algorithm = sys.argv[1]
    runAlgorithm(algorithm) 
    


if __name__ == "__main__":
    main()