#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import graphviz as gv
import sys

class Node(object):

    def __init__(self, val):
        self.data = val
        self.left_child = None
        self.right_child = None
        self.parent = None
        self.node_id = None

    def setVal(self, val):
        self.data = val

    def setLeftChild(self, node):
        self.left_child = node
        self.left_child.parent = self

    def setRightChild(self, node):
        self.right_child = node
        self.right_child.parent = self

    def __str__(self):
        return '[D:%d , L:%s , R:%s]' % (self.data,self.left_child.data,self.right_child.data)


class BST(object):

    def __init__(self):
        self.root = None
        


    def print_tree(self):
        self.__print_tree(self.root)

    def find(self, key):
        return self.__find(self.root, key)

    def render(self):
        self.viz = gv.Digraph(format='png')
        self.node_id = 0
        self.__build_viz(self.root)
        self.viz.render('bst.png')
        print(self.viz.source)
        
    def __build_viz(self,root,parent=None):
        if root == None and parent:
            self.viz.node(str(self.node_id),'*',shape='point',color='gray')
            self.viz.edge(str(parent.node_id),str(self.node_id),arrowhead='box',arrowsize='.5' )
            self.node_id += 1
        if root == None:
            return
        else:
            if not root.node_id:
                root.node_id = self.node_id
                self.node_id += 1
                self.viz.node(str(root.node_id),str(root.data))
            if parent:
                self.viz.edge(str(parent.node_id),str(root.node_id))
            self.__build_viz(root.left_child,root)
            self.__build_viz(root.right_child,root)


    def insert(self, data):

        # if no root exists
        if self.root == None:
            self.root = Node(data)
        else:
            # otherwise find location to insert
            parent = self.root
            temp = self.root
            direction = ''

            # Loop until we find a "null" child pointer then insert
            while not temp == None:
                parent = temp
                if temp.data > data:
                    direction = 'left'
                    temp = temp.left_child
                else:
                    direction = 'right'
                    temp = temp.right_child

            # Update parent pointer.
            if direction == 'left':
                parent.left_child = Node(data)
                parent.left_child.parent = parent

            else:
                parent.right_child = Node(data)
                parent.right_child.parent = parent



    def __find(self, root, key):
        while True:
            if root == None:
                return None
            elif root.data == key:
                return root
            elif root.data > key:
                root = root.left_child
            else:
                root = root.right_child


    def __print_tree(self, root):
        if root == None:
            return
        else:
            self.__print_tree(root.left_child)
            print root.data
            self.__print_tree(root.right_child)


def bin_order(L):
    newL = []
    if len(L) == 0:
        return
    else:
        bin_order(leftside)
        bin_order(rightside)


#random.seed(97697)

tree = BST()
L = [int(1000 * random.random()) for i in xrange(100)]

#L = sorted(L)

tree.insert(500)
for i in L:
   tree.insert(i)

tree.render()


			
