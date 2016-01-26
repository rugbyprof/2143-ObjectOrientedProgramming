# Homework 1 - Getting your python feet wet

### Requirements
- Add an `add` method to the simple fraction class below
- If you were to run the following code snippet:

```python
a = fraction(1,2)
b = fraction(4,5)
c = a * b
print(c)
```
it would print out:
```
1 3/10
```

```python
import os
import time


class fraction(object):
    def __init__(self,n=None,d=None):
        self.numerator = n
        self.denominator = d
        
    def __str__(self):
        return "%s / %s" % (self.numerator , self.denominator)
        
    def numerator(self,n):
        self.numerator = n 
        
    def denominator(self,d):
        self.denominator = d
        
    def __mul__(self,rhs):
        x = self.numerator * rhs.numerator
        y = self.denominator * rhs.denominator
        return fraction(x,y)
   
      
    

if __name__ == '__main__':
    a = fraction(1,2)
    b = fraction(4,5)
    c = a * b
    print(c)
```
