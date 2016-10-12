# Not Done


## Ineritance

Let’s explore another powerful object-oriented programming tool: inheritance. Suppose
we want to write `Dog` and `Cat` classes. Here’s our first attempt:

```python
class Dog(object):
    def __init__(self, name, owner, color):
        self.name = name
        self.owner = owner
        self.color = color
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")
    def talk(self):
        return self.name + " says woof!"

class Cat(object):
    def __init__(self, name, owner, lives=9):
        self.name = name
        self.owner = owner
        self.lives = lives
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")
    def talk(self):
        return self.name + " says meow!"
```

Notice that both the `Dog` and `Cat` classes have `name`, `owner`, `eat` method, and `talk` methods. 
That’s a lot of effort for so much repeated code!

This is where inheritance comes in. In Python, a class can inherit the instance variables
and methods of a another class without having to type them all out again. For example:

```python
class Foo(object):
    # This is the superclass
    
class Bar(Foo):
    # This is the subclass
```

`Bar` inherits from `Foo`. We call Foo the `superclass` (the class that is being inherited) and
Bar the `subclass` (the class that does the inheriting).

Notice that Foo also inherits from the object class. In Python, `object` is the top-level
superclass; everything inherits from it, whether directly or through other superclasses.
object provides basic functionality that is needed for other classes to work with Python.

### When should we use inheritance?

One common use of inheritance is to represent a hierarchical relationship between two or
more classes – one class is a more specific version of the other class. For example, dogs
are a specific type of pet, and a pet is a specific type of animal.

Using inheritance, here is a second attempt at representing dogs.

```python
class Pet(object):
    def __init__(self, name, owner):
        self.is_alive = True # It’s alive!!!
        self.name = name
        self.owner = owner
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")
    def talk(self):
        print(’...’)
        
class Dog(Pet):
    def __init__(self, name, owner, color):
        Pet.__init__(self, name, owner)
        self.color = color
    def talk(self):
        print(’woof!’)
```

Notice that, by using inheritance, we did not have to redefine `self.name`, `self.owner`,
or the `eat` method. We did, however, redefine the talk method in the `Dog` class. In this
case, we want `Dogs` to `talk` differently, so we override the method.

The line `Pet. init (self, name, owner)` in the `Dog` class is necessary for inheriting
the instance attributes `self.is_alive`, `self.name`, and `self.owner`. Without
this line,`Dog` will never inherit those instance attributes. Notice that when we call
`Pet__init__`, we need to pass in self, since `Pet` is a class, not an instance.
