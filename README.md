# Blackjack-Win-Rate-Simulation
A blackjack simulation program to determine the win, lose and tie probability of n games.

# Rules of Blackjack
Blackjack is a game in which a player plays against a dealer. Both the player and the dealer try to get cards that add up to as high a number as possible without crossing 21. Crossing 21 means you automatically lose. If both the player and the dealer both cross 21, the dealer wins. However, the player can see one of the dealer’s cards before making their decision, whereas the dealer acts independently of the player’s cards, generally continuing until its score hits 17.
Each numerical card (2–10) is worth its number, an ace is worth 1 or 11, a face card is worth 10. Note that this means there are effectively 4 times as many 10s (10, J, Q,K) as other cards. There are various other caveats, like blackjack bonuses, splits, and doubles.
The dealer will always have a face up card at the start of the round.
But in this project, we will be ignoring blackjack bonuses, splits and doubles.

# Project Overview and Instruction
* There are two variables in the program. These can be changed to desired values.
  * Code Line 11 - numGame
  * Code Line 12 - strategy
* "numGame" is the number of games. (The intial program simulated with 1 million games)
* "strategy" is the specific strategy to run the simulation. There are four strategies. (type in "Strategy 1", "Strategy 2",
"Strategy 4" or "Strategy 4"). The 'S' of Strategy should be captitalized followed by a space and a number ranging from 1 to 4).

# Strategy
Dealer will be using a fixed strategy. The dealer will always get a card if the total score of dealer is under 17, which means the dealer will not draw a card if the total score of dealer is 17 or above.

There are four strategies used by the player. (which can be changed in the code)
## Strategy 1
The player will get exactly two cards only. The score of both the player and dealer will be added and evaluted to determin win, lose or tie. 
## Strategy 2
The player will draw card if the total score of player is under 17. The player will stop drawing card if the total score of player is 17 or over.
## Strategy 3
This strategy is the same as Strategy 2 but there is an extra condition. The extra condition is if the dealer face up card has a value of 10 and player score is 17, the player will draw an extra card.
## Strategy 4
If the player total score is less than 2 times the dealer face up and player total score is less than 16, the player always draw.

# Simulation result
The probablity of win, tie and lose of 'n' number of blackjack games.

## Number of games = 1 million
![screenshot3](https://user-images.githubusercontent.com/55210396/76239375-7672a100-61ff-11ea-8ee9-6ccd7ca0ffca.png)

## Number of games = 10 million (It takes around 15 minutes to run each strategy)
![screenshot4](https://user-images.githubusercontent.com/55210396/76239491-ade14d80-61ff-11ea-8a02-5a31305a606a.png)

# Environment 
Python 3.7 is needed to run [blackjack3.py](blackjack3.py). Download [Python 3.7](https://www.python.org/downloads/) here and install it.

# Conclustion
The result of the four strategies indicate that the player has more chance to lose in a blackjack game. 

# Project Expansion
There are many more basic blackjack strategy not implemented in the project. For a better and more accurate simulation results, more strategies could be combined into a more complicated codes to yeild more accurate outcomes.
