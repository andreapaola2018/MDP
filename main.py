import sys

def runAlgorithm(algorithm): 
    if algorithm == "MC": 
        print("MC")
        pass
    elif algorithm == "VI": 
        pass
    elif algorithm == "QL": 
        pass

##user will input algorithm name in command line 
def main():
    algorithm = sys.argv[1]
    runAlgorithm(algorithm) 
    


if __name__ == "__main__":
    main()