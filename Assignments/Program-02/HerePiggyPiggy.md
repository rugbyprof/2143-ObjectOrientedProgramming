# Program 2 - Gaming Strategy Simulation
Due: TBD

## Program Overview

You are going to determine the best strategy for playing the dice game pig. By simulating thousands of rounds of games, we can see which strategy would maximize a players odds for winning. The basic game class has been written, and what you need to do is create a player class that will represent a player, thier score, and thier strategy. Below is a basic explanation of the game "pig" that we have been discussing in class.

### Pig

The game was introduced by John Scarne, a magician and game developer, in 1945 and it has since been played with a wide range of variants to the original concept. Over the years, there have been a number of commercial productions of Pig, with titles like Skunk and Pig Dice, as well as the most current version, Pass the Pig. It has also served as a fun and useful tool for math teachers who are trying to convey probability concepts to young students and for computer science instructors, as well.

### How to Play Basic Pig

Pig requires at least two players and it can, conceivably, be played by as many people as you have available. The only things that you’ll need to have are a standard, six-sided die, a piece of paper and something to write with.

Every time that a player rolls in Pig, they have to make a decision about their next move that could cost them the win. If they have rolled any number from a 2 to a 6, they are free to collect points that are equal to the face value of their roll and they can roll again, or they can decide to take the points and hold, handing the die over to the next player. If the player makes the call to decide to roll again and a 1 comes up, the points that they had from their initial roll are taken away, their turn is over, and their score for that round is a zero. For as long as they don’t roll a 1 though, the player can continue to throw the dice and to accumulate points. The players take turns this way until one of them reaches 100 points and is declared the winner.

In an example, if a player’s first three rolls come up as a 4, a 2, and a 3, and they opt to hold, they will receive nine points for that turn, because 4 + 2 + 3 = 9. If they decided to continue rolling and their fourth throw yielded a 1 on the die however, those nine points would be wiped out and their score for that round would be a zero.

<sup>Source: http://dicegames.org/pig/</sup>

## Model vs Simulation 

A computer model is the algorithms and equations used to capture the behavior of the system being modeled. By contrast, computer simulation is the actual running of the program that contains these equations or algorithms. Simulation, therefore, is the process of running a model. Thus one would not "build a simulation"; instead, one would "build a model", and then either "run the model" or equivalently "run a simulation".

<sup>Source: https://en.wikipedia.org/wiki/Computer_simulation</sup>

## Game Play Styles (Strategies)

- Categories
    - Aggressive 
    - Cautious
    - Robust
    - Copycat
- Strategies
    - Target Score
    - Target Rolls
    - Sprint to Finish
    - Mimic Opponent
    - Situational

### Target Score

This simply picks a target score for each turn. For example the value 20 seemed to work well in our simple experiments in class. We could adjust this score up or down to see there is any improvement in outcome.

### Target Rolls

The player will roll a "target" number of times every time unless a skunk value occurs. Again, we could adjust this target up or down to see there is any improvement in outcome.

### Sprint To Finish

This strategy could be employed with one of the above strategies (Target Score, Target Rolls), with the addition of the "sprint". If the player comes within _**X**_ points of finishing the game, they will continue to roll until they encounter a skunk, or finish. 

> Note: The implementation of this could be a little fuzzy. For example lets define our "sprint" threshold as 72. If our current score is 55, and in our current turn we achieve the "sprint" score, do we keep going? If we skunk out we go back to 55. OR if we have 55 do we employ our current strategy (no matter if we get to 72 or not) then the NEXT turn if we are 72 or greater we can sprint to the end. 

### Mimic Opponent

Count your oppenents rolls, or avg points per turn, and copy their actions. This may take a few turns to figure out, so an initial strategy may need to be employed. 

### Situational

We decided that this strategy would be "conservative" if they were ahead of their opponent, or "aggressive" if they were behind their opponent. This could get a little hard if we are playing with more than one opponent. 



## Requirements

- Create a folder called _**program\_2**_.
- Create a file called _**driver.py**_ within _**program\_2**_ that is a copy of the given file [game_starter.py](./game_starter.py)
-  

 