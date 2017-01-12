import random
import sys
import locale


initialFunds = 100.0
winProbability = 0.5  #probability of a win
period = 20 #number of times bet will be made 
rounds = 1000000 # number of rounds to exicute
costPerbet = 0
b = 1 #units won per unit bet
a = 0.5 #units lost per unit bet

random.seed()

kellyFraction = (winProbability*(a + b) - a)/(a*b) 

fraction = kellyFraction #fraction of current funds to wager
cutLossesPoint = 5 #Level of current funds to cut losses and quit

successes = 0 #number of rounds with current funds > initial funds
successRate = 0 #success/rounds
kellySR = 0 #Kelly success rate
kellyAT = 0 #Kelly avg funds

largestTake = 0
lowestTake = 100

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def calculate():
    global successes 
    global successRate
    global kellySR
    global kellyAT
    global largestTake
    global lowestTake
    successes = 0
    sumOfFunds = 0
    largestTake = 0
    lowestTake = 100
    random.seed()

    for i in range(0, rounds):
        currentFunds = initialFunds
    
        for i in range(0, period):
            if(random.uniform(0,1) < winProbability):
                 outcome = b
            else:
                 outcome = -a

            bet = currentFunds*fraction
            currentFunds = currentFunds + bet*outcome
            currentFunds = currentFunds - costPerbet
            if( currentFunds < cutLossesPoint):
                # print(bcolors.RED + "RUIN!" + bcolors.ENDC)
                break
        
        if(currentFunds > initialFunds):
            successes = successes + 1
        sumOfFunds = sumOfFunds + currentFunds
        if(currentFunds > largestTake):
            largestTake = currentFunds
        if(currentFunds < lowestTake):
            lowestTake = currentFunds

    successRate = successes/rounds
    avgFunds = sumOfFunds/rounds

    if(fraction == kellyFraction):
        print(bcolors.RED + "\nFraction used (kelly): ", round(fraction, 3))
        print("        Success rate = " , successRate)
        print("        Average take = ", locale.format("%d", round(avgFunds - initialFunds, 2), grouping=True), "or ", round((avgFunds - initialFunds)/initialFunds , 2), " fold increase")
        print("        Largest Take = ", locale.format("%d", round(largestTake,2), grouping=True), " lowest remaining funds = ", round(lowestTake, 2))
        if(successRate < 0.5):
            print("        !!!!FAIL!!!!")
        print(bcolors.ENDC)
        kellySR = successRate;
        kellyAT = round(avgFunds - initialFunds, 2)
    
    elif((successRate > kellySR) and (round(avgFunds - initialFunds, 2) > kellyAT)):
        print(bcolors.OKBLUE + "\nFraction used: ", round(fraction, 3))
        print("        Success rate = " , successRate)
        print("        Average take = ", locale.format("%d", round(avgFunds - initialFunds, 2), grouping=True), "or ", round((avgFunds - initialFunds)/initialFunds , 2), " fold increase")
        print("        Largest Take = ", locale.format("%d", round(largestTake,2), grouping=True), " lowest remaining funds = ", round(lowestTake, 2))
        if(successRate < 0.5):
            print("        !!!!FAIL!!!!")
        print(bcolors.ENDC)
    
    else:
        print("\nFraction used: ", round(fraction, 3))
        print("        Success rate = " , successRate)
        print("        Average take = ", locale.format("%d", round(avgFunds - initialFunds, 2), grouping=True), "or ", round((avgFunds - initialFunds)/initialFunds , 2), " fold increase")
        print("        Largest Take = ", locale.format("%d", round(largestTake,2), grouping=True), " lowest remaining funds = ", round(lowestTake, 2))
        if(successRate < 0.5):
            print(bcolors.RED + "        !!!!FAIL!!!!" + bcolors.ENDC)
    sys.stdout.flush()

locale.setlocale(locale.LC_ALL, '')
print("starting ")
print("Win probability:         ", winProbability)
print("Max number of bets:      ", period)
print("Number of trials:        ", locale.format("%d", rounds, grouping=True))
print("initial funds:           ", initialFunds)
print("Units won per unit bet:  ", b)
print("Units lost per unit bet: ", a)
print("Cost per bet:            ", costPerbet)
sys.stdout.flush()

# delta = b-a
# print("delta: ", delta, " success prob ", successRate)
# i = 0
# r = 0
# while (winProbability > 0):
#     winProbability = winProbability - 0.05
#     kellyFraction = round((winProbability*(a + b) - a)/(a*b) , 4)
#     fraction = kellyFraction
#     if(fraction < 0):
#       break;
#     calculate()
#     print(successRate)
#     sys.stdout.flush()
#     i = i + 1

calculate()

fraction = kellyFraction + 0.2*kellyFraction
initialFunds = initialFunds
calculate()

fraction = kellyFraction + 0.1*kellyFraction
initialFunds = initialFunds
calculate()

fraction = kellyFraction - 0.1*kellyFraction
initialFunds = initialFunds
calculate()

fraction = kellyFraction - 0.2*kellyFraction
initialFunds = initialFunds
calculate()
