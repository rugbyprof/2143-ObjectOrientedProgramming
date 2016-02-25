
--
Consider this program:
```python
L = [4, 10, 8]
x = L.sort()
L.append(20)
L2 = L[1:]
```

Fill in the Python Shell output after this program has executed.
```
>>> x

```

```
>>> L


```


```
>>> id(L) == id(L2)


```
--

See the phone pad below:

![](https://s3.amazonaws.com/f.cl.ly/items/2O371F2t1U422A3m340S/225px-telephone-keypad.jpg)

Write a function called `alphaToNumeric` that receives an 'alphanumeric' phone number and returns a numeric (9 digit) phone number. For example: XH0EZQI70A = 9403974702. You can solve this anyway you want. If the input to the function is not 9 characters/digits return `None`. The list below is a hint at one way to approach the problem.



```python
alpha = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

```

--

Would the previous function solution have been better with a dictionary? Explain.

--

Write a function called `guessAnswer` that will guess the correct answer and return the number of guesses that were necessary. This function receives 3 values: 
- `low`: lowest value that answer could be (inclusive)
- `high`: highest value that answer could be (inclusive)
- `answer`: the correct answer

Your function should find the answer in less than O(N) time. Meaning you shouldn't loop from low -> high testing every value. 

--

Try turning your `guessAnswer` function into a class that actually runs a game. 

--

#### Airplane & Flight Class

- Develop two classes to keep track of airplanes and flights.
- Here is the header and docstring for class Airplane.

```python
class Airplane:
"""
Information about a particular airplane including the model, the serial
number, the number of seats, and the number of miles travelled.
"""
```


####Constructor

Complete the `__init__` method for our Airplane class:

```python
def __init__(self, plane_model, serial_num, num_seats, miles_travelled):
""" 
@Description:
	Record the airplane's model plane_model, serial number serial_num, the
	number of seats, and the distance travelled miles_travelled.
@params: 
	plane_model (string) - type of plane (e.g. Boing 747)
	serial_num (int) - 
	num_seats (int) - 
	miles_travelled (float) - total number of miles plane has travelled.
@Returns: None
"""












```

Here is some usage and its output:

```python
airplane = Airplane('Boeing 747', '19643', 366, 45267.7)

print(airplane.model)
# Prints: 'Boeing 747'
print(airplane.serial)
# Prints: '19643'
print(airplane.seats)
# Prints: 366
print(airplane.miles)
# Prints: 45267.7
```

--

#### \_\_str__ Method

Write a `__str__` method for  class Airplane that returns strings of this form: 'Airplane(Boeing 747, 19643, 366, 45267.7)'



#### Adding a Method to Airplane Class

- Below is a description for method `log_trip` in our class `Airplane`. 
- Write the body of the method.
- Add an example that creates an Airplane object, logs a trip of 1000.0 miles, and shows that
those miles have been logged. 

```python
def log_trip(self, num_miles):
""" 
@Description: Adds n miles to the planes total miles flown where n > 0
@Param: num_miles (float) - number of miles to add to the total
@Returns: None
"""










```

Example Here:
```
















```
#### Overloading an Operator

Write an `__eq__` method in class `Airplane` that compares two Airplane objects to see if they are equal.

Consider two Airplanes equal if they have the same serial number. 



--

#### Class Flight

```python
""" 
@Description: Information about an airplane flight. 

"""
class Flight:

    def __init__(self, plane):
    """ 
    @Description: Create a Flight with an empty passenger list on airplane plane.
    @Param: plane (Airplane) - the airplane in which to keep track of flight information.
    @Returns: None
"""










```

Example Usage:
```python
a = Airplane('Boeing 747', '19643', 366, 45267.7)
f = Flight(a)
print(f.airplane)
# Print: 'Airplane(Boeing 747, 19643, 366, 45267.7)'
print(f.passengers)
#Prints: []
```


#### Add Method to Flight Class

Complete method add in class Flight.

```python
def add(self, passenger):
""" 
@Description: If there are still seats available on this flight, add passenger to the
passenger list. 
@Params: passenger (string) - passenger name
@Returns: (bool) True iff passenger is added to this flight.













```

Example Usage:
```python
a = Airplane('Cessna 150E', '9378', 1, 824.8)
f = Flight(a)
print(f.add('Myrto'))
#Prints: True
print(f.add('Jen'))
#Prints: False
```

-- 

#### Misc

Write a class called `wordDictonary` that represents an actual dictionary. Your class should contain the following methods:
- `loadDictionary` : 
    - reads a file that contains `word: definition` 
    - a word may occur more than once (same word alternate definition)
    - you should be able to hold all definitions
- `updateDictionary`:
    - a method that lets you add a word:definition to the class
- `findWord`:
    - this method receives a word, and returns all definitions that correspond to it. 
- `removeWord`:
    - this method lets you remove a word from the dictionary. 
    
--

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
	# Start with a copy of the list so we don’t modify the original.
	L = L[:]









```

### Coffee Class 
A coffee shop lets customers purchase coffee with pre-loaded electronic cards. They can reload their cards
by specifying an amount of money to be added. Each card is also programmed with a default dollar amount
that gets reloaded when the purchaser does not specify an amount.

#### Defining the class
- Write the constructor with the appropriate data members needed to keep track of 
    - defualt reload amount
    - current amount on the card
- Write the reload method that allows the user to reload the card with a specified amount.
- Write the default reload method that will reload the card with the default amount.
- Write the buy_coffee method, which has a parameter indicating the amount paid.
    - If the card has enough money to cover the purchase, the amount is deducted.
    - If the card does not have enough money to cover the purchase, the balance is unchanged. 
    - Return True iff the card had enough money to cover the purchase.

There may some additional things you need to add to your class depending on the user stories (the way
the class is used) below.

#### Using the class
- Create a card for Karen with an initial balance of $100 and a default reload value of $50.
    - e.g.(card_for_karen = Card("Karen", 100, 50))
- Have Karen buy 25 coffees at a cost of $2.50 each.
- Create a card for Sven with an initial balance of $50 and a
    - default reload value of $20.
- Have Sven buy a fancy coffee at a cost of $5.
- Reload Karen’s card with her default reload value.
- Have Sven put an additional $5.75 on his card.
- Print the owner and balance of both cards.


#### Dictionary

Use a dictionary to help you create a list of unique values. Lets say I asked you to create a list of integers between 0-99999 that is entirely unique, but you couldn't use `in` to check and see if the value was already in the list. You also can't use sets like so: `myNums = list(set(myNums))`. So, use a dicionary to help keep your items unique. 
