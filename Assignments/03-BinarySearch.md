
# Program 1 - Binary Search

## Not Done

### Overview

You are going to write your first class in python. This class will treat a list as if it's a "Binary Tree". 
To do this you simply have to follow a set of rules in how you place items into your list. First, however,
lets discuss what a binary tree is. 

### Binary Tree

![](http://cramster-image.s3.amazonaws.com/definitions/computerscience-5-img-1.png)

A `Binary Tree` is a data structure (or a `Graph`) that organizes data such that:
- Each `node` can have at most two `child` nodes 
- A node can have 0,1 or 2 children. 
- Nodes that have zero children are `leaves`. 
- The node where the tree originates is the `root`. 
- Non leaf nodes are called `inner nodes`

A `Binary Search Tree` is a data structure (or a `Graph`) that organizes data such that:

- It follows the same structure as a Binary Tree, however,
- The child node on the left must contain a value that is less than it's parent 
- Likewise the child on the right must contain a value that is greater than it's parent. 
- Placing the same key values in a Binary Tree is possible, but lets assume unique keys for now.

### Binary Search Tree as An Array


### Corresponding Tree Locations
![](https://s3.amazonaws.com/f.cl.ly/items/3l1f1s0q07343t2J1W01/binary_tree_table.png)

Another way to look at it:

![](http://www.brpreiss.com/books/opus4/html/img1458.gif)

1. Don't use the first element location in the list (leave the 0<sup>th</sup> element empty).
    - This helps with our 

### Requirements
- Add an `add` method to the simple fraction class below
- If you were to run the following code snippet:

```python
a = fraction(1,2)
b = fraction(4,5)
c = a + b
print(c)
```
it would print out:
```
1 3/10
```
it should not print out:

```
13/10
```

- This means we need to handle:
    - a `whole number` portion of a fraction.
    - ability to reduce 

### Deliverables
