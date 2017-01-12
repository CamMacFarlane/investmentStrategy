# investmentStrategy
A project for Computer Engineering 461 Design and Analysis of Computer Networks
A python script to simulate investing in a stock with a known outcome probability. 
The script shows that the Kelly Strategy (https://en.wikipedia.org/wiki/Kelly_criterion") is optimal in ideal situaitons but for more realistic situations (a fee is charged per transaction for example) some adjustment is needed. 
Use:
Adjsut any of the following variables and observe the results, using < 100k rounds is not reccomended 

initalFunds - inital funds to use
winProbability - probability of a win
period  - number of times bet will be made 
rounds - number of rounds to exicute
costPerbet - cost per bet 
b - units won per unit bet
a - units lost per unit bet
