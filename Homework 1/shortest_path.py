#####################################################################################
# CS 5112 HW 1 - Dijkstra's Algorithm
# shortest_path.py
# Authors: Sungseo Park and Varun Narayan
# Date: 09/05/2018
#
# Implementation of Dijkstra's algorithm to find the shortest path between two nodes
# in a graph. Assuming that the path exists and all edge weights are positive.
#####################################################################################

def shortest_path(graph, source, target):
  # `graph` is an object that provides a get_neighbors(node) method that returns
  # a list of (node, weight) edges. both of your graph implementations should be
  # valid inputs. you may assume that the input graph is connected, and that all
  # edges in the graph have positive edge weights.
  # 
  # `source` and `target` are both nodes in the input graph. you may assume that
  # at least one path exists from the source node to the target node.
  #
  # this method should return a tuple that looks like
  # ([`source`, ..., `target`], `length`), where the first element is a list of
  # nodes representing the shortest path from the source to the target (in
  # order) and the second element is the length of that path
  #
  # NOTE: Please see instructions.txt for additional information about the
  # return value of this method.

  # discovered = [] -> tuple of node and path to the node, closest length so far
  # structure: {node: (length, [path])}
  discovered = {}
  discovered[source] = (0, [])

  # queue = [] -> list of nodes and potential path to node and length of potential path
  # structure of tuple: (node,length,[path])
  queue = []

  # initially populate with neighbors of source
  tempList = graph.get_neighbors(source)
  for k in tempList:
    queue.append((k[0], k[1], [source, k[0]]))

  # Loop through until target is in discovered
  while target not in discovered:
  # Take the edge off the queue with the shortest path length
    temp = queue[0]
    for i in queue[1:]:
      if i[1] < temp[1]:
        temp = i
    queue.remove(temp)

  # Explore and add if not already in discovered
    if temp[0] not in discovered:
      currentNode = temp[0]
      discovered[currentNode] = (temp[1], temp[2])

      # Add the neighbors 
      neighborsList = graph.get_neighbors(currentNode)
      for i in neighborsList:
        newNode = i[0]
        newDist = i[1] + discovered[currentNode][0]
        oldPath = discovered[currentNode][1]
   
        newPath  = []
        for i in oldPath:
          newPath.append(i)
        newPath.append(newNode)
        queue.append((newNode, newDist, newPath))

  return (discovered[target][1], discovered[target][0])
