#### Not Done

### Dictionaries
- Count the number of occurrences of words in a string using a dictionary as your container. The code we discussed in class is [HERE](https://github.com/rugbyprof/2143-ObjectOrientedProgramming/blob/master/ClassLectures/day3b.py).  Assume there is a string
called `words` that is space delimited and has NO punctuation. 

Given:
```python
words = "the the and the and and and the boy boy the and boy boy and and and end"
```

Result:
```python
{'the': 5,'and': 8,'boy': 4,'end': 1 }
```

-----


### Python Lists / Functions

- Complete the function using this algorithm: 
    - continually remove the largest and smallest values from the list and return either the last value (if there is only one left) or the average of the two last values (if there are two left).
    - Do not sort the list, and don't use any for loops in your solution. 
    - Functions `max` and `min` may be helpful, as well as one or more list methods.

```python
def myMedian(L):
""" 
@Description: Return the median of the numbers in L.
@Params: L (list)
@Returns: median (int)
"""










```
-----

### Class Definitions

Be able to write a fraction class and overload the `addition` and `multiplication` operators. I will provide a GCD method. Make sure you implement the `str` method so a fraction prints out correctly.

-----


### Color Class

- Create a class called "Color" that will store a tuple of (r,g,b). 
- The tuple should be stored in a data member called color.
- The components of the color tuple should be stored in data members: red, green, blue as well 
- Add a __str__ method to print out the color class so it looks like: "(red: redVal, green: greenVal, blue: blueVal)"
- Here is some usage:

```python

c1 = Color((255,0,0))
print(c1.red)
#prints: 255

c1.blue = 255
print(c1)
#prints: (red: 255, green: 0, blue: 255)

c1.color = (0,0,0)
print(c1)
#prints: (red: 0, green: 0, blue: 0)

```

-----

Overload the addition operator so that we can add two colors. Adding colors is a pretty wierd experience, so we will create our own addition method. Basically we will average each color. 

For example:

```python

c1 = (255,255,255)
c2 = (0,0,0)
c3 = c1 + c2

print(c3)
#prints: (128,128,128)
```

-----

### Grayscale Class

This class will ***extend*** the color class.

So what is gray scale? Its where you take the 3 individual parts of a color and using those values you calculate a single value that will be assigned to each of the 3 components, making it some shade of gray.
 
For example here is red: `(0,255,0)` and here is the gray scale equivalent: `(85,85,85)` (using the average method from below).

Your `GrayScaler` class is serious about its grayscalin` powers and has three methods to turn a color into its monochromatic equivalent:
- lightness
- average
- luminosity
- custom

**Lightness**

The lightness method averages the most prominent and least prominent colors: `(max(R, G, B) + min(R, G, B)) / 2`.

**Average**

The average method simply averages the values: `(R + G + B) / 3`.

**Luminosity**

This method also averages the values, but it forms a weighted average to account for human perception. We’re more sensitive to green than other colors, so green is weighted most heavily. The formula for luminosity is `0.21 * R + 0.72 * G + 0.07 * B`

**Custom**

This method allows the user to pass in three floats to act as the weights in your formula: `w1 * R + w2 * G + w3 * B`

Here is some example usage to help you determine how to design your class:

```python

myColor = (255,0,0)
grayish = GrayScaler(myColor)
gray1 = grayish.Average()
gray2 = grayish.Custom(.33,.44,.23)


grayish2 = GrayScaler() # defaults to black in the class if no color provided
grayish2.SetColor(255,192,203)
gray3 = grayish2.Luminosity()
```

```python
"""
@Description: Gets an RGB color represented as a tuple, and converts it to a 
				gray scale equivalent based on chosen method.
@Methods:
    Lightness - as described above
    Average - as described above
    Luminosity - as described above
    Custom - as described above
    SetColor - Lets user change the color originally passed in.
"""
class GrayScaler(Color):













```
