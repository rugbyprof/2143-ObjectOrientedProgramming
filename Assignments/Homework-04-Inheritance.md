# Not Done

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
