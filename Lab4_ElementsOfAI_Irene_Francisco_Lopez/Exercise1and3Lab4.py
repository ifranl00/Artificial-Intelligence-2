# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 03:45:29 2021

@author: irene

Lab 4- Exercise 1
    Implementing Depth First Search (DFS) algorithm 
    Consider the graph below and note the expected orders of traversal for this graph using DFS.

Answer: the expected order could be A,B,E,I,C,F,J,G,D,H following the rules that are also implemented in the program bellow (exercise 3 of the lab):
    - Starting from the A node, we pick all of them and recur on their adjacents.
    - We stop when all nodes are visited in this case because we want to know the order of traversal, not to find one specific node.


Lab 4- Exercise 3

DFS - a recursive method
 Implement the Depth First Search algorithm using a popular problem-solving approach called recursion.
 Pointer:Define a base case inside the method that follows the following rule: If the given leaf node has already been visited, the algorithm needs to backtrack’.
 
 Answer: in the code below, our expected orders obtained in the exercise 1, can be checked.
 
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

visitedNodes = set() # The nodes that are already visited to know when to finish the algorithm

def dfsAlgorithm(visitedNodes, tree, node):
    if node not in visitedNodes: # Keep running until all the nodes are visited
        print (node) # The node is printed so we can know the orders of traversal
        visitedNodes.add(node) # Each node visited is added
        for neighbour in graph[node]: 
            dfsAlgorithm(visitedNodes, graph, neighbour) # recursive call to the method with the updated visited nodes list

# Finally we call the method which starts at A node to execute it
dfsAlgorithm(visitedNodes, graph, 'A')

# The expected orders calculated whitout running the program are the same that which are contained in the output printed out by console.

