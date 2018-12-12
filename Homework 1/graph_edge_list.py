#####################################################################################
# CS 5112 HW 1 - Dijkstra's Algorithm
# graph_adjacency_list.py
# Authors: Sungseo Park and Varun Narayan
# Date: 09/05/2018
#
# An implementation of a weighted, directed graph as an edge list. This means
# that it's represented as a list of tuples, with each tuple representing an
# edge in the graph.
#####################################################################################

class Graph:
  def __init__(self):
    # DO NOT EDIT THIS CONSTRUCTOR
    self.graph = []

  def add_edge(self, node1, node2, weight):
    # Adds a directed edge from `node1` to `node2` to the graph with weight
    # defined by `weight`.
    # check if edge already exists, if so remove it
    for i in self.graph:
      if i[:2] == (node1,node2):
        self.graph.remove(i)
        break
    # add the new edge
    self.graph.append((node1, node2, weight))

  def has_edge(self, node1, node2):
    # Returns whether the graph contains an edge from `node1` to `node2`.
    # DO NOT EDIT THIS METHOD
    return (node1, node2) in [(x,y) for (x,y,z) in self.graph]

  def get_neighbors(self, node):
    # Returns the neighbors of `node` as a list of tuples [(x, y), ...] where
    # `x` is the neighbor node, and `y` is the weight of the edge from `node`
    # to `x`.
    # define empty adjacency list
    adj_list = []
    # since it is a directed graph, you need to check for tuples where the first 
    # entry is the same as node
    for i in self.graph:
      if (i[0]==node):
      # add neighbor and weight to the list
        adj_list.append(i[1:])
    # return adj_list
    return adj_list

  def print_graph(self):
    print(self.graph)