
# Program 1 - Binary Search

## Not Done

### Overview

You are going to write your first class in python. This class will treat a list as if it's a "Binary Search Tree". 
Why? Because a Binary Search Tree allows an item to be found in O(lg N) time, whereas a list or an array only
allows searches to be completed in O(N) time. 

To make a a list function as a Binary Search Tree, we simply need to follow a set of rules in how items into the list. Then we follow
the same rules in reverse to locate an item in the list in O(lg N) time. 

First, lets do a small overview of a Binary Search Tree.

### Binary Tree

![](http://cramster-image.s3.amazonaws.com/definitions/computerscience-5-img-1.png)

A `Binary Tree` is a hierarchical data structure (or a `Graph`) that organizes data such that:
- A node can have 0,1 or 2 children (two children is what makes it a 'binary' tree).
- Nodes that have zero children are `leaves`. 
- The node where the tree originates is the `root`. 
- Non leaf nodes are called `inner nodes`
- More definitions later

A `Binary Search Tree` is a data structure (or a `Graph`) that organizes data such that:

- It follows the same structure as a Binary Tree, however,
- The child node on the left must contain a value that is less than it's parent 
- Likewise the child on the right must contain a value that is greater than it's parent. 
- Placing the same key values in a Binary Tree is possible, but lets assume unique keys for now.

### Binary Search Tree as An Array (List)

We determine the location of items in the list by using the following method:

1. Do not use the first list element. Zero messes things up.
2. If the list is empty, place item at the 1<sup>st</sup> location.
3. Each subsequent item to be inserted gets compared with the root and the next location gets calculated:
    - if its less than: 
        - Left Child = 2*i (where i == index into list)
    - if its greater than:
        - Right Child - 2*i+1 
4. If that location is occupied, then keep comparing until an empty spot is found.



![](https://s3.amazonaws.com/f.cl.ly/items/2d0j1r030M1P3m28050c/array_bst.png)

### Corresponding Tree Locations

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
