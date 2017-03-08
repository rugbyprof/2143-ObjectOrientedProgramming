#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import graphviz as gv


if __name__=='__main__':

    viz = gv.Digraph(format='png')
    node_id = 0

        
    data = ('1')
    viz.node(data)
                
    viz.render('bst.png')