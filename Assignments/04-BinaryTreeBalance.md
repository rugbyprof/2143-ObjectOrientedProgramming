# Homework 4 - Binary Tree Balanced Loading
Due on github by ***Thursday March 10<sup>rd</sup>*** by class time. 

### Overview
- Working by yourself, or with a partner, alter the `BinarySearch` class so that its perfectly balanced after loading a random set of integers. Also, there should be no duplicate key values in the tree.

### Requirements
- Create a folder called `BalancedBinaryTree` for all your files.
- Rename `binary_search_tree_list.py` to  `balanced_binary_tree.py`.
- Rename the `BinarySearch` class to `BalancedSearch`.
- Alter the BalancedSearch class so that it results in a balanced binary tree representation of a given set of integers.
- Ask the user "Load how many random numbers? ", then load that amount of numbers into the tree.
- Alter the insert method so that it receives a `list` instead of an `int`:
- 
```python
@Name: insert
@Description:
    Receives a list of unordered integers and inserts them into the binary tree in such a manner that the resulting tree is balanced.
@Params:
    values (List) - unorderd list of integers
@Returns: None
```

***Additional Helper Code***

```python

# Create a list to hold unique integers
unique = []

# loop 1000 times
for x in range(1000):

    # get a random number
    r = random.randint(0,99999)
    
    # if it's not already in the list, enter it.
    if r not in unique:
        unique.append(r)

# Sort the list
unique.sort()

```

## Starter Code:
Code can be found [here](https://github.com/rugbyprof/2143-ObjectOrientedProgramming/blob/master/binary_search_tree_list.py).

### Deliverables

- Upload everything to gitHub this means the folder and all it's contents named correctly.
- The file should execute with no errors.
- If you worked with a partner, both people should have the code in thier repo.
- Your name (or both names) should be in all documents.
- Comment, Comment, Comment ....

