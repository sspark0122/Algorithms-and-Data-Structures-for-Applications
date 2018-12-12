###########################################################################
# CS 5112 HW 3 - Huffman and Boyer-Moore
# Authors: Sungseo Park and Varun Narayan
# Python 2.7
# Date: 10/13/18
###########################################################################
from operator import attrgetter

class HuffmanTree:
  # Inner class to help build the tree
  class TreeNode:
    def __init__ (self, left = None, right = None, symbol = None, min_element = None, weight = None):
      self.left = left
      self.right = right
      self.symbol = symbol
      self.min_element = min_element
      self.weight = weight

  # The`symbol_list` argument is a list of tuples `(symbol, weight)`,
  # where `symbol` is a symbol that can be encoded, and `weight` is the
  # the unnormalized probabilitiy of that symbol appearing.
  def __init__(self, symbol_list):
    assert(len(symbol_list) >= 2)

    self.root = None # (place TreeNode object here)
    self.encoding = {}

    # Convert all symbols into TreeNode leaves in list
    nodeList = []
    for sym, w in symbol_list:
      nodeList.append(self.TreeNode(symbol = sym, min_element = sym, weight = w))

    # While the lists length is > 1
    while len(nodeList) > 1:
    # Take out lowest two weighted objects and combine
      nodeList = sorted(nodeList, key = attrgetter('weight','min_element'))
      smallNodes = nodeList[:2]
      newNode = self.combineSubTrees(smallNodes[0],smallNodes[1])
      
      # Add new root node into list
      nodeList.append(newNode)
      nodeList = nodeList[2:]
    
    # When len == 1, set self.root to that variable
    self.root = nodeList[0]

    # Create encoding dict
    self.createDict("", self.root)


  # Encodes a string of characters into a string of bits using the
  # symbol/weight list provided.
  def encode(self, s):
    assert(s is not None)
    # Encode each character separately
    outputString = ""
    for i in s:
      outputString += self.encoding[i]

    return outputString

  # Decodes a string of bits into a string of characters using the
  # symbol/weight list provided.
  def decode(self,s):
    assert(s is not None)
    outputString = ""
    currNode = self.root

    for i in s:
      if i == "0":
        currNode = currNode.left
      else:
        currNode = currNode.right
      # Tried to go down an impossible path
      if currNode == None:
        return None
      if currNode.symbol != None:
        outputString += currNode.symbol
        currNode = self.root

    # Didn't get to the end of the tree, therefore, not properly decoded
    if currNode != self.root:
      return None

    return outputString

  # Pass in TreeNodes, pass in so nodes are ordered
  def combineSubTrees(self, nLeft, nRight):
    return self.TreeNode(left = nLeft, right = nRight, 
      weight = nLeft.weight + nRight.weight, 
      min_element=min(nLeft.min_element,nRight.min_element))

  # Recursively pass through the tree and construct the encoding dict
  def createDict(self, string, node):
    if node == None:
      return

    if node.symbol != None:
      self.encoding[node.symbol] = string
      return

    self.createDict(string + "0", node.left)
    self.createDict(string + "1", node.right)