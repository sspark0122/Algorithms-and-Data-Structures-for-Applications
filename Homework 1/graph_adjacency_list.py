#####################################################################################
# CS 5112 HW 1 - Dijkstra's Algorithm
# graph_adjacency_list.py
# Authors: Sungseo Park and Varun Narayan
# Date: 09/05/2018
#
# An implementation of a weighted, directed graph as an adjacency list. This
# means that it's represented as a map from each node to a list of it's
# respective adjacent nodes.
#####################################################################################
class Graph:
  def __init__(self):
    # DO NOT EDIT THIS CONSTRUCTOR
    self.graph = {}

  def add_edge(self, node1, node2, weight):
    # Adds a directed edge from `node1` to `node2` to the graph with weight
    # defined by `weight`.
    # if the key doesn't exist in the dict, then create a new list and add
    if node1 not in self.graph:
      adj_list = [(node2,weight)]
      self.graph[node1] = adj_list
      return

    # if the node exists, check for node2 and remove if it exists
    temp_list = self.graph[node1]
    for i in temp_list:
      if i[0] == node2:
        temp_list.remove(i)
    temp_list.append((node2,weight))
    self.graph[node1] = temp_list

  def has_edge(self, node1, node2):
    # Returns whether the graph contains an edge from `node1` to `node2`.
    # DO NOT EDIT THIS METHOD
    if node1 not in self.graph:
      return False
    return node2 in [x for (x,i) in self.graph[node1]]

  def get_neighbors(self, node):
    # Returns the neighbors of `node` as a list of tuples [(x, y), ...] where
    # `x` is the neighbor node, and `y` is the weight of the edge from `node`
    # to `x`.
    if node not in self.graph:
      return []
    return self.graph[node]
