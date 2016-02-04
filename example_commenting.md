# Python Documentation Requirements 

This is how I want you to comment your code for class. Every program should have something similar
to this. It's not `pythonic` at all, but oh well. Python programmers have thier own way of doing things. 
I just created a format that shows clearly (to me) an overview of what your program does and requires (for
usage). Hopefully it will also force you to "think" a little bit about design before you actually start coding. 

### Program Comment Block
```python
"""
Program:
--------
    Short Title  - Long Title

Description:
------------
    This would be a short description of your program and a general overview of what you did. 
    Should be about a paragraph, depending on the program.
    
Name: Joanna Culpepper
Date: 3 Feb 2016
"""
```

### Class Comment Block

**Definition**

```python
"""
Class:
------
    This is just the name of your class 
    Usage: example class declaration here
    
Description:
------------
    This would be a short description of your class and a general overview of what it does. 

Params:
-------
    param1 - (type) All these are parameters that you passed into your class (possibly) to help construct the class
    param2 - (type) They should be alphebetized
    param3 - (type)

Methods:
--------
    Alphebetize the methods here...
    High level descriptions and usage here. This is a quick view for you or someone who's using your class so 
    they know what methods are available, and how to use them. If they need more, they can go look at the method
    itself.
    method1 - description
        usage: example1 use here
    method1 - description
        usage: example2 use here
"""
```

**Example**

```python
from types import *

"""
Class:
------
    MyFraction 
    f1 = MyFraction(2,3)    # creates 2/3
    f2 = MyFraction()       # creates None/None
    
Description:
------------
    This is a class that assists in the general creation and manipulation of fractions. It provides overloaded operators
    to assist in basic arithmetic operations between fractions.

Params:
-------
    denominator  - (int) a denominator value or None
    numerator    - (int) a numerator value or None

Methods:
--------
    add - Add two fractions
        usage:  f3 = MyFraction(2,3) + MyFraction(1,2)
                f4 = f1 + f2
    sub - Subtract two fractions
        usage: same as add but use a + :)
    
    mul - Multiply two fractions
        usage: same as add but use a * :)
    
    div - Divide two fractions
        usage: same as add but use a / :)
"""
class MyFraction:
    def __init__(numerator=None,denominator=None):
        assert (type(numerator) is int or numerator == None) , "Assertion: numerator bad value: %d" % (n)
        assert (type(denominator) is int or denominator == None) , "Assertion: denominator bad value: %d" % (n)
        assert (denominator != 0) , "Assertion: divide by zero!" 
        
        self.numerator = numerator
        self.denominator = denominator
    
```

### Method Comment Block

```python

def mul(rhs):
    """
    Description:
    ------------
        This method multiplys a passed in fraction to self, without altering self and passes back a new fraction
        It does not reduce the resulting fraction. 
    
    Params:
    -------
        rhs - (MyFraction) The right hand side of the operation
    
    Returns:
    --------
        (MyFraction) - result of operation
    """
    
    return MyFraction(self.numerator*rhs.numerator,self.denominator*rhs.denominator)
    
```
