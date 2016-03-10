
def alphanumeric(num):
    num = list(num)
    if len(num) != 9:
        return None
    
    alpha = ['','ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
    
    phone = ""
    
    for i in num:
        for chunk in alpha:
            if i in chunk:
                print(alpha.index(chunk))
                phone += str(alpha.index(chunk))
    
    return phone
              
  
def alphanumeric(num):
    num = list(num)
    if len(num) != 9:
        return None
    
    alpha = ['','ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
    
    phone = []
    
    for i in num:
        for chunk in alpha:
            if i in chunk:
                print(alpha.index(chunk))
                phone.append(alpha.index(chunk))
    
    return ''.join([str(i) for i in phone])
    
def guessAnswer(low,high,answer):
    guesses = 0
    for i in range(low,high+1):
        if answer == i:
            return guesses + 1
        guesses += 1

    
  
def guessAnswer2(low,high,answer,guesses=1):
    
    start = (low + high) // 2
    
    print(start,low,high)
    if answer == start:
        return guesses
    elif answer > start:
        return guessAnswer2(start+1,high,answer,guesses+1)
    else:
        return guessAnswer2(low,start-1,answer,guesses+1)

class wordDictonary(object):
    def __init__(self):
        self.words = {}
        f = open('words.txt', 'r')
        for line in f:
            word,definition = line.split(':')
            definition = definition.strip("\n")
            
            if not word in self.words:
                self.words[word] = []
            
            self.words[word].append(definition)

                

    def printDictionary(self):
        for k in self.words:
            print(k,self.words[k])
  
if __name__=='__main__':
    #print(alphanumeric('ABCFFGZMX'))

    # L = ['a','b','c','d','e']
    # print(L.index('c'))
    
    # print(guessAnswer(1,10923140192340,1923874))
    # print(guessAnswer2(1,10923140192340,1923874))   
    d = wordDictonary()
    d.printDictionary()
    
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

    self.plane_model = plane_model
    self.serial_num = serial_num
    self.num_seats = num_seats
    self.miles_travelled = miles_traveled
```

--

#### \_\_str__ Method

Write a `__str__` method for class Airplane that returns strings of this form: 'Airplane(Boeing 747, 19643, 366, 45267.7)'

```python
def __str__(self):
    return "%s %d %d %f" % (self.plane_model,self.serial_num,self.num_seats,self.miles_travelled)
```

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

    self.miles_travelled += num_miles


```

Example Here:
```
airplane = Airplane('Boeing 747', '19643', 366, 45267.7)
airplane.log_trip(1000.0)
print(airplane)

```

#### Overloading an Operator

Write an `__eq__` method in class `Airplane` that compares two Airplane objects to see if they are equal.

Consider two Airplanes equal if they have the same serial number. 


```python
def __eq__(self,rhs):
    return self.serial_num == rhs.serial_num
    
```

--
