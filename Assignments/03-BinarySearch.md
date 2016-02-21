
# Program 1 - Binary Search

### Overview

You are going to write your first class in python. This class will treat a list as if it's a "Binary Tree". 
To do this you simply have to follow a set of rules in how you place items into your list. First, however,
lets discuss what a binary tree is. 

### Binary Tree

![](http://cramster-image.s3.amazonaws.com/definitions/computerscience-5-img-1.png)

A Binary Tree is a data structure (or a `Graph`) that organizes data such that each `Node` can have at most two `Child` nodes. A node can have 0,1 or 2 children. Nodes that have zero children are `leaves`. The node where the tree originates is the `root`. You can see an example of a binary tree structure below. 

A Binary __Search__ Tree is a data structure (or a `Graph`) that organizes data such that each `Node` can have at most two `Child` nodes AND that the child node on the left must contain a value that is less than it's parent and likewise the child on the right must contain a value that is greater than it's parent. Placing two values in a Binary Tree is possible, but let's not discuss that now. 

### Binary Search Tree as An Array

![](https://s3.amazonaws.com/f.cl.ly/items/3m020U1u1f0s2j1t3f3A/binary_tree.png)

You can see the binary tree above contains 12 items numbered 0 - 11. In this specific example the values are inserted in such a way that the tree is being filled in from left to right. Inserting values in this way creates a `complete` tree. This means that every `inner node` (non leaf node) has either all of its children, or a left child. 

### Corresponding Tree Locations
![](https://s3.amazonaws.com/f.cl.ly/items/3l1f1s0q07343t2J1W01/binary_tree_table.png)

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
