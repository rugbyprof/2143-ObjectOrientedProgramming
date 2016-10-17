# Program 2 - Gaming Strategy Simulation
Due: TBD

## Program Overview

In the simplest terms, we are writing a game program. Our program will contain the necessary components for us to play the game "Pig" (described below). But this is a computer science class, so lets go beyond simple game implementation.

We are going to enhance the game play by implementing a set of strategies within the game. Right now, for each turn, we simply roll the dice for some random number of rolls. This could be considered a strategy, albeit a really bad one. A simple improvement on this could be to roll a set number of times, or try to achieve a set score each time, or even better, base your decision on the current game state! This won't be as hard to implement as you think. 

Once we enhance our gameplay by adding strategy, then we are going to run a simulation to decide which strategy, or set of strategies is the best choice. Don't get intimidated by anything described here. You will see that what is being proposed is extremely doable.



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


