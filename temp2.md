```python
"""
Name: James Torres
Email: james.torres@outlook.com
Assignment: Homework 1 - Lists and Dictionaries
Due: 31 Jan @ 11:00 a.m.
"""
#A: What would Python print?

a = [1, 5, 4, 2, 3] 
print(a[0], a[-1])
# Prints: 1 3

a[4] = a[2] + a[-2]
print(a)
# Prints: [1, 5, 4, 2, 6]

print(len(a))
# Prints: 5

print(4 in a)
# Prints: True

a[1] = [a[1], a[0]]
print(a)
# Prints: [1, [5, 1], 4, 2, 6]

#B: Write a function that removes all instances of an element from a list.

"""def remove_all(el, lst):
Removes all instances of el from lst. 
Given: x = [3, 1, 2, 1, 5, 1, 1, 7]
Usage: remove_all(1, x)
Would result in: [3, 2, 5, 7]
   pass"""

x = [3, 1, 2, 1, 5, 1, 1, 7]
print (x)

def remove_all():
    while 1 in x:
         x.remove(1)
      
remove_all()
print (x)

"""
C: Write a function that takes in two values, x and y, and a list, and adds as many y's to the end of the list as there are x's. Do not use the built-in function count.
 def add_this_many(x, y, lst):
 Adds y to the end of lst the number of times x occurs in lst. 
Given: lst = [1, 2, 4, 2, 1]
Usage: add_this_many(1, 5, lst)
Results in: [1, 2, 4, 2, 1, 5, 5]
   pass"""

def add_this_many(x, y, lst):
    for i in lst:
      if  i == x:
         lst.append(y)
add_this_many(1, 5, lst)
print (lst)

a = [3, 1, 4, 2, 5, 3]
print(a[:4])
# Prints: [3, 1, 4, 2]

print(a)
# Prints: [3, 1, 4, 2, 5, 3]

print(a[1::2])
# Prints: [1, 2, 3]

print(a[:])
# Prints: [3, 1, 4, 2, 5, 3]

print(a[4:2])
# Prints: []

print(a[1:-2])
# Prints: [1, 4, 2]

print(a[::-1])
# Prints: [3, 5, 2, 4, 1, 3]

"""E: Let's reverse Python lists in place, meaning mutate the passed in list itself, instead of returning a new list. We didn't discuss this in class directly, so feel free to use google. Why is the "in place" solution preferred?
def reverse(lst):
Reverses lst in place. 
Given: x = [3, 2, 4, 5, 1] 
Usage: reverse(x)
Results: [1, 5, 4, 2, 3]
   pass"""

x = [3, 2, 4, 5, 1]

def reverse(x):
   for i in range(len(x)//2):
       swap = x[i]
         x[i] = x[len(x)-(i + 1)]
         x[len(x)-(i + 1)] = swap
reverse(x)
print (x)

"""F. Write a function that rotates the elements of a list to the right by k. Elements should not ”fall off”; they should wrap around the beginning of the list. rotate should return a new list. To make a list of n 0's,you can do this: [0] * n
def rotate(lst, k):
 Return a new list, with the same elements of lst, rotated to the right k.
Given: x = [1, 2, 3, 4, 5]
Usage: rotate(x, 3)
Results: [3, 4, 5, 1, 2]
    pass"""

x = [1, 2, 3, 4, 5]

def rotate(x, k):
   return x[(k-1):] + x[:(k-1)]
   
xrot = rotate(x, 3)
print(xrot)

# had to get help from Chris Duhan(pretty nice eh?)

print ()


superbowls = {'joe montana': 4, 'tom brady':3, 'joe flacco': 0}
print(superbowls['tom brady'])
# Prints: 3

superbowls['peyton manning'] = 1
print(superbowls)
""" Prints: {'peyton manning': 1, 'tom brady': 3, 'joe flacco': 0, 'joe montana': 4}"""

superbowls['joe flacco'] = 1
print(superbowls)
""" Prints:{'peyton manning': 1, 'tom brady': 3, 'joe flacco': 1, 'joe montana': 4}"""

print()  
 # H: Continuing from above, what would Python print?

print('colin kaepernick' in superbowls)
#Prints: False

print(len(superbowls))
#Prints: 4

print(superbowls['peyton manning'] == superbowls['joe montana'])
#Prints: False

superbowls[('eli manning', 'giants')] = 2
print(superbowls)
"""Prints: {'joe flacco': 1, 'tom brady': 3, ('eli manning', 'giants'): 2, 'peyton manning': 1, 'joe montana': 4}"""

superbowls[3] = 'cat'
print(superbowls)
#Prints: {'tom brady': 3, 3: 'cat', ('eli manning', 'giants'): 2, 'peyton manning': 1, 'joe montana': 4, 'joe flacco': 1}


superbowls[('eli manning', 'giants')] =  superbowls['joe montana'] + superbowls['peyton manning']
print(superbowls)
#Prints: {'tom brady': 3, 3: 'cat', ('eli manning', 'giants'): 5, 'peyton manning': 1, 'joe montana': 4, 'joe flacco': 1}

superbowls[('steelers', '49ers')] = 11
print(superbowls)
#Prints: {'tom brady': 3, 3: 'cat', ('eli manning', 'giants'): 5, 'peyton manning': 1, ('steelers', '49ers'): 11, 'joe montana': 4, 'joe flacco': 1}

print()

"""I: Given a dictionary replace all occurrences of x as the value with y.
def replace_all(d, x, y):
Replaces all values of x with y. 
Given: d = {1: {2:3, 3:4}, 2:{4:4, 5:3}} 
Usage: replace_all(d,3,1)
Results: {1: {2: 1, 3: 4}, 2: {4: 4, 5: 1}} 
    pass"""
    
d = {1: {2:3, 3:4}, 2:{4:4, 5:3}}

def replace_all(d, x, y):
   for k in d.keys():
      if type(d[k]) is dict:
      replace_all(d[k], x, y)
      elif d[k] is x:
      d[k] = y
      
replace_all(d, 3, 1)
print(d)
print()

"""J: Given a (non-nested) dictionary delete all occurences of a value. You cannot delete items in a dictionary as you are iterating through it (google :) ).
def rm(d, x):
Removes all pairs with value x. 
Given:  d = {1:2, 2:3, 3:2, 4:3}
Usage:  rm(d,2)
Results: {2:3, 4:3}
    pass """
    
d = {1:2, 2:3, 3:2, 4:3}
def rm(d, x):
   lst = []
   for k in d.keys():
   if d[k] is x:
      lst.append(k)
   for k in lst:
   del d[k]
   
rm(d, 2)
    
print(d)
```
