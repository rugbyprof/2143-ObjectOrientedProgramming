
# Program 1 - Binary Search Class

## Not Done!

### Overview

You are going to write a binary search class in Python. This class will treat a list as if it's a "Binary Search Tree" (BST). 
Why? Because a BST allows an item to be found in *O(lg N)* time, whereas a list or an array only allows searches to be completed in *O(N)* time. 

To make a a list function as a BST, we simply need to follow a set of rules in how items are inserted into the list. Then we follow the same rules in reverse to locate or retrieve an item in *O(lg N)* time. 

Before we start creating our class, lets do some background on Binary Trees in general. 


>***Note:*** Remember that a `Binary Tree` is NOT the same thing as a `Binary Search Tree`. A search tree has an implied ordering that we can utilize to make searches fast. Without this ordering, we simply have a plain ol' binary tree and finding things would take *O(N)* time (meaning we would have to look at possibly every single item).



### Binary Tree
![](https://s3.amazonaws.com/f.cl.ly/items/0U3y1n1U2d0O191w421D/binary_tree.png)


A `Binary Tree` is a hierarchical data structure (or a `Graph`) that organizes data such that:
- A node can have 0,1 or 2 children (two children is what makes it a 'binary' tree).
- Nodes that have zero children are `leaves`. 
- The node where the tree originates is the `root`. 
- Non leaf nodes are called `inner nodes`
- More definitions later

### Binary Search Tree

![](https://s3.amazonaws.com/f.cl.ly/items/2l1N0U0M362v3v2b3f03/binary_search_tree.png)

A `Binary Search Tree` is a data structure (or a `Graph`) that organizes data such that:

- It follows the same structure as a Binary Tree, however,
- The child node on the left must contain a value that is less than it's parent 
- Likewise the child on the right must contain a value that is greater than it's parent. 
- Placing the same key values in a Binary Tree is possible, but lets assume unique keys for now.

***Recursion***

The definition about the left child having a value less than it's parent and the right child having a value that's greater than it's parent recurses down through the entire tree. Basically you can grab any node (along with all its children) and you have a brand new binary tree. By removing the root node with key 9 from the original tree, we've just created two new BST's that fulfill all the rules of a BST. This is an important concept because we will soon learn to manipulate BST's via recursion. 


![](https://s3.amazonaws.com/f.cl.ly/items/1Q3j1Y1T430D2d1v2647/binary_search_trees.png)

***Key***

A key value is the value that determines whether an item gets placed on the left or the right of its parent. We like to make things simple in our CS classes (hence small integers in the nodes), but a single node in a Binary Search Tree can hold hundreds or thousands of items. And to find that node with the hundreds or thousands of items, we need a search key!
 


### Binary Search Tree as An Array (List)

So we now know that a Binary Search Tree can hold all kinds of data, and that we can find said data (using a search key) in O(lg N) time. Now we need to know how to implement (or create) a BST. Hopefully from your last course you remember that a data structure can be implemented in two ways: 

1. List Based
2. Array Based

(explain difference between the confusion of list in C++ is not list in Python)

We determine where to place items (and how to find items) in the list by using the following method:

1. Do not use the first list element. The zero index messes things up.
2. If the list is empty, place item at the 1<sup>st</sup> index location.
3. Each subsequent item to be inserted gets compared with the root and the next location gets calculated:
    - if its less than: 
        - Left Child = 2*i (where i = index into list)
    - if its greater than:
        - Right Child - 2*i+1 (again where i = index into list)
4. If that location is occupied, then keep comparing until an empty spot is found.

#### Example:

Lets place the items 



![](https://s3.amazonaws.com/f.cl.ly/items/2d0j1r030M1P3m28050c/array_bst.png)

### Corresponding Tree Locations

![](http://www.brpreiss.com/books/opus4/html/img1458.gif)

1. Don't use the first element location in the list (leave the 0<sup>th</sup> element empty).
    - This helps with our 

### Requirements


### Deliverables
