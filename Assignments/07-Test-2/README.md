Test 2 Study Guide
==================

## Q1

Read the following: [Inheritance](https://github.com/rugbyprof/2143-ObjectOrientedProgramming/blob/master/ztrunk/fall.16/inheritence_explanation.md)

Also, go look at this: https://inst.eecs.berkeley.edu/~cs61a/fa14/lab/lab06/


## Q2

### Candy Class

Create a set of classes that represent the following:

- A bag/box of candy
- A case of the above
- Inventory of our candy

Determine whether to use inheritence or composition as the relationship between classes. Use the information given below to guide your class creation:

- ***Candy Class*** 
    - Attributes
        - key
        - name of candy
        - bag or box
        - num items per bag or box
        - cost per item
        - cost per bag or box
    - Methods
        - ?
- ***Case Class***
    - Attributes
        - weight
        - number of bags or boxes
        - cost per case as a discount percentage (e.g. .22)
    - Methods
        - ?
- ***Inventory Class***
    - Attributes
        - uses a dictionary to track items or cases of items
    - Methods:
        - `AddItem(int key,string name,float price,int amount)`
            - adds an item(s) to your inventory
            - returns None
        - `SellItem(int key,int amount)`
            - sells (subtracts) a amount of items from inventory.
            - returns cost of selling that many item(s).
        
## Q3

Create a `point class`, `line class`, and a `rectangle class`. 

- A point is a tuple of two integers: `(3,6)`
    - Add a move point method that receives: *dx*,*dy* which are the amounts of change to apply to the point. Example: *(-2,2)* would turn the point *(3,6)* into *(1,8)*.
- A line consists of two points: `(3,6),(7,8)`
    - Add a length method that returns the length of a line.
- A rectangle consists of two points as well, the upper right, and the lower left.
    - Add an area and perimeter method 

## Q4

Given an email class to represent an email: 
```python
class Email(object):
	def __init__(self, msg, subj, sender, receiver):
		self.message = msg
		self.subject = subj
		self.sender = sender 	#email address
		self.receiver = receiver #email address
```

- Write a class called "EmailLogger" that will keep track of all emails sent and received by each user. 
- Do you need to extend the Email class? Or use composition.
- Create 2 containers: `emails_sent` and `emails_received` that would let you obtain a list of emails when you pass in an email address.
- The method `get_sent_by` would receive an email address as input and return a list of emails sent by that user.
- The method `get_received_by` would receive an email address as input and return a list of emails received by that user. 

Usage:
```
Logger = EmailLogger()

Email1 = Email("fake message 1","fake subject 1","joe@yahoo.com","sue@gmail.com")
Logger.add(Email1)

Email2 = Email("fake message 2","fake subject 2","bill@yahoo.com","sue@gmail.com")
Logger.add(Email2)

Email3 = Email("fake message 3","fake subject 3","bill@yahoo.com","joe@yahoo.com")
Logger.add(Email3)

Email4 = Email("fake message 4","fake subject 4","jon@hotmail.com","sue@gmail.com")
Logger.add(Email4)


list1 = Logger.get_sent_by("bill@yahoo.com")
# list1 = [Email2,Email3]

list2 = Logger.get_received_by("sue@gmail.com")
# list2 = [Email1,Email2,Email4]
```

Your answer should be a complete class that would fulfill the usage example above.

## Q5

```python
def pigify(w):
 """Returns: copy of w converted to Pig Latin 'y' is a vowel if it is not the first letter 
 If word begins with a vowel, append 'hay'
 If word starts with 'q', assume followed by 'u'; move 'qu' to the end, and append 'ay'
 If word begins with a consonant, move all consonants up to first vowel to end and add 'ay'
 Precondition: w contains only (lowercase) letters"""
 
 
 
 
 
 ```

## Q6

```
def replace(thelist,a,b):
 """Returns: A COPY of thelist with all occurrences of a replaced by b.
 Example: replace([1,2,3,1], 1, 4) = [4,2,3,4].

 Precondition: thelist is a list of ints; a and b are ints
 returns a [] 
 """
 
 
 
 
 ```
