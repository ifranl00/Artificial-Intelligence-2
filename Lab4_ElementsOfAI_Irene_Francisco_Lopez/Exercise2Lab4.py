# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 03:45:29 2021

@author: irene

Lab 4- Exercise 2
    DFS - a non-recursive approach
        Implement a method in Python that accepts a graph and traverses through it using DFS.
        Pointers:
            - Define this graph as an adjacency list using the Python dictionary.
            - Use a stack and a list to keep track of the visited nodes.
            - The defined method should take the dictionary representing the graph and a source node as input. 
"""
graph = { # To store the adjacent of each node
    'A' : ['B','C','D'],
    'B' : ['E'],
    'C' : ['F','G'],
    'D' : ['H'],
    'E' : ['I'],
    'F' : ['J'],
    'G' : [],
    'H' : [],
    'I' : [],
    'J' : []
}


def dfsAlgorithm(graph, node):
    stack = [node] 
    visitedNodes = set() # The nodes that are already visited to know when to finish the algorithm

    while stack:
        node = stack.pop() # add the current node to the top of the stack
        if node not in visitedNodes: # if current node is not visited
            visitedNodes.add(node);
            print (node) # The node is printed so we can know the orders of traversal
            stack.extend(reversed(graph[node])) # extend the list appending the node from a iterable that must the one returned by reversed to keep the order of the visited nodes
# Finally we call the method which starts at A node to execute it
dfsAlgorithm(graph, 'A')

# The expected orders calculated whitout running the program are the same that which are contained in the output printed out by console.

