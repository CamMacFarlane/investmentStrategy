# investmentStrategy
<h1>A project for Computer Engineering 461 Design and Analysis of Computer Networks</h1>
<p>
A python script to simulate investing in a stock with a known outcome probability. 
The script shows that the Kelly Strategy (https://en.wikipedia.org/wiki/Kelly_criterion") is optimal in ideal situaitons but for more realistic situations (a fee is charged per transaction for example) some adjustment is needed. 
</p>
<h3>Use:</h3>
<p>Adjust any of the following variables and observe the results, using less than 100k rounds is not recommended </p>
<ul>
<li>initialFunds - initial funds to use</li>
<li>winProbability - probability of a win</li>
<li>period  - number of times bet will be made</li> 
<li>rounds - number of rounds to execute</li>
<li>costPerbet - cost per bet </li>
<li>b - units won per unit bet</li>
<li>a - units lost per unit bet</li>
</ul>

<p>
If the output for a fraction variant is shown in blue it means that both the average take and the win probability for this simulation were higher than those of the kelly fraction. (The fraction variant performed better than the Kelly Fraction)
</p>



