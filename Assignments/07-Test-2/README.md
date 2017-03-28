Test 2 Study Guide
==================

## Q1

Read the following: [Inheritance](https://github.com/rugbyprof/2143-ObjectOrientedProgramming/blob/master/ztrunk/fall.16/inheritence_explanation.md)


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
