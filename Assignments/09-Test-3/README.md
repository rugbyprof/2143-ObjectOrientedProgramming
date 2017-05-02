## Q1

Once upon a time, on a way through the old wild west,…

… a man was given directions to go from one point to another. The directions were "NORTH", "SOUTH", "WEST", "EAST". 
Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too. Going to one direction and coming back the opposite 
direction is a needless effort. Since this is the wild west, with dreadfull weather and not much water, it's important 
to save yourself some energy, otherwise you might die of thirst!

How I crossed the desert the smart way.

The directions given to the man are, for example, the following:

`["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]`.
or
`{ "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" }`

You can immediatly see that going "NORTH" and then "SOUTH" is not reasonable, better stay to the same place! So the task is to 
give to the man a simplified version of the plan. A better plan in this case is simply:

`["WEST"]`
or
`{ "WEST" }`


In `["NORTH", "SOUTH", "EAST", "WEST"]`, the direction "NORTH" + "SOUTH" is going north and coming back right away. What a waste of 
time! Better to do nothing.

The path becomes `["EAST", "WEST"]`, now "EAST" and "WEST" annihilate each other, therefore, the final result is `[]`.

In `["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"]`, "NORTH" and "SOUTH" are not directly opposite but they become directly 
opposite after the reduction of "EAST" and "WEST" so the whole path is reducible to `["WEST", "WEST"]`.

#### Task

Write a function dirReduc which will take an array of strings and returns an array of strings with the needless directions 
removed (W<->E or S<->N side by side).

#### Examples

```python
dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]) => ["WEST"]
dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH"]) => []
```
Note

All paths can't be made simpler. The path `["NORTH", "WEST", "SOUTH", "EAST"]` is not reducible. 
"NORTH" and "WEST", "WEST" and "SOUTH", "SOUTH" and "EAST" are not directly opposite of each other and can't become such. 
Hence the result path is itself : `["NORTH", "WEST", "SOUTH", "EAST"]`.

## Q2
The new "Avengers" movie has just been released! There are a lot of people at the cinema box office 
standing in a huge line. Each of them has a single 100, 50 or 25 dollars bill. A "Avengers" ticket 
costs 25 dollars.

Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

Can Vasya sell a ticket to each person and give the change if he initially has no money and sells the 
tickets strictly in the order people follow in the line?

Return YES, if Vasya can sell a ticket to each person and give the change. Otherwise return NO.

#### Examples:

```python
tickets([25, 25, 50]) # => YES 
tickets([25, 100]) # => NO. Vasya will not have enough money to give change to 100 dollars
```

## Q3

Define a class named Shape and its subclass Square. The Square class has an init function which takes a 
length as argument. Both classes have a area function which can print the area of the shape where Shape's 
area is 0 by default.

Hints:

To override a method in super class, we can define a method with the same name in the super class.


### Example:
```python
aSquare= Square(3)
print aSquare.area()
```

## Q4

Counting Duplicate Letters

Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphanumeric characters, including digits, uppercase and lowercase alphabets.

Example

- "abcde" -> 0 # no characters repeats more than once
- "aabbcde" -> 2 # 'a' and 'b'
- "aabbcdeB" -> 2 # 'a' and 'b'
- "indivisibility" -> 1 # 'i'
- "Indivisibilities" -> 2 # 'i' and 's'
- "aa11" -> 2 # 'a' and '1'

## Q5

Your task is to find the first element of an array that is not consecutive.

E.g. If we have an array `[1,2,3,4,6,7,8]` then 1 then 2 then 3 then 4 are all consecutive but 6 is not, so that's the first non consecutive number.

If the whole array is consecutive then return `null`

The array will always have at least 2 elements and all the elements will be numbers. The numbers will also all be unique and in ascending order. The numbers could be positive or negetive and the first non-consecutive could be either too!

## Q6

Roulette Wheel
![](http://farm9.staticflickr.com/8089/8370772707_6e0b6d13e2.jpg)


Roulette Table

![](http://www.itmaybeahack.com/book/oodesign-python-2.1/html/_images/Roulette2.png)
