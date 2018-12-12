###########################################################################
# CS 5112 HW 2 - Hash Tables
# Authors: Sungseo Park and Varun Narayan
# Python 3
# Date: 9/20/18
###########################################################################
#!PYTHON3
# Please see instructions.pdf for the description of this problem.
from fixed_size_array import FixedSizeArray
from cs5112_hash import cs5112_hash1

# Implementation of a node in a singlely linked list.
# DO NOT EDIT THIS CLASS
class SLLNode:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node

  def set_next(self, node):
    self.next_node = node

  def get_next(self):
    return self.next_node

  def set_value(self, value):
    self.value = value

  def get_value(self):
    return self.value

# An implementation of a hash table that uses chaining to handle collisions.
class HashTable:
  def __init__(self, initial_size=10, load_factor=.75):
    # DO NOT EDIT THIS CONSTRUCTOR
    if (initial_size < 0) or (load_factor <= 0) or (load_factor > 1):
      raise Exception("size must be greater than zero, and load factor must be between 0 and 1")
    self.array_size = initial_size
    self.load_factor = load_factor
    self.item_count = 0
    self.array = FixedSizeArray(initial_size)

  # Inserts the `(key, value)` pair into the hash table, overwriting any value
  # previously associated with `key`.
  # Note: Neither `key` nor `value` may be None (an exception will be raised)
  def insert(self, key, value):
    # if key or value is None, raise an Exception
    if (key == None or value == None):
      raise ValueError("Neither Key nor Value can be None")

    # Get the hash value and take the modulus
    hashval = cs5112_hash1(key) % self.array_size

    # If there is nothing at that entry in the array, create the first node and inc count
    if (self.array.get(hashval) == None):
      newNode = SLLNode((key,value))
      self.array.set(hashval, newNode)
      self.item_count += 1
    else:
    # If something already exists, iterate through and see if any match the key
      node = self.array.get(hashval)
      prevNode = None

      while (node != None):
        # If so, update the value and don't change the count
        if (node.get_value()[0] == key):
          node.set_value((key,value))
          return
        prevNode = node
        node = node.get_next()

      # Else at the end add the node and inc the count
      newNode = SLLNode((key,value),None)
      prevNode.set_next(newNode)
      self.item_count += 1

    # If the load factor now exceeds the limit, resize
    if ((float(self.item_count)/self.array_size) > self.load_factor):
      self._resize_array()

  # Returns the value associated with `key` in the hash table, or None if no
  # such value is found.
  # Note: `key` may not be None (an exception will be raised)
  def get(self, key):
    # If key is None, raise an Exception
    if (key == None):
      raise ValueError("Key can't be None")

    # Get hash value and mod it
    hashval = cs5112_hash1(key) % self.array_size
    node = self.array.get(hashval)

    # While 'node' isn't None, search through
    while (node != None):
      if (node.get_value()[0] == key):
        return node.get_value()[1]
      node = node.get_next()

    # Else return None
    return None

  # Removes the `(key, value)` pair matching the given `key` from the map, if it
  # exists. If such a pair exists in the map, the return value will be the value
  # that was removed. If no such value exists, the method will return None.
  # Note: `key` may not be None (an exception will be raised)
  def remove(self, key):
    # If key is None, raise an Exception
    if (key == None):
      raise ValueError("Key can't be None")

    # Get hash value and mod it
    hashval = cs5112_hash1(key) % self.array_size

    node = self.array.get(hashval)
    # Can't remove it if it doesn't exist
    if (node == None):
      return None

    # If it is the first element of the linked list, set that pointer to the next
    if (node.get_value()[0] == key):
      self.array.set(hashval, node.get_next())
      self.item_count -= 1
      return node.get_value()[1]

    prevNode = node
    node = node.get_next()

    # While 'node' isn't None, search through 
    while (node != None):
    # If it is found further down the list, set the previous node's 
    # pointer to the next node and return the value
      if (node.get_value()[0] == key):
        prevNode.set_next(node.get_next())
        self.item_count -= 1
        return node.get_value()[1]
      prevNode = node
      node = node.get_next()

    # Else return None
    return None

  # Returns the number of elements in the hash table.
  def size(self):
    return self.item_count

  # Internal helper function for resizing the hash table's array once the ratio
  # of stored mappings to array size exceeds the specified load factor.
  def _resize_array(self):    
    tupList = []
    # Iterate through all of the items in the previous array and add to a list
    for i in range(self.array_size):
      node = self.array.get(i)
      while (node != None):
        tupList.append(node.get_value())
        node = node.get_next()

    # Replace self.array with the new array
    self.array = FixedSizeArray(self.array_size*2)
    self.array_size *= 2
    self.item_count = 0

    # Iterate through the list of tuples and add them back
    for (k, v) in tupList:
      self.insert(k, v)

  # Internal helper function for accessing the array underlying the hash table.
  def _get_array(self):
    # DO NOT EDIT THIS FUNCTION
    return self.array

# Helper print function to investigate inner workings of structure
  # def printArray(self):
  #   print("[", end = '')
  #   for i in range(self.array_size):
  #     node = self.array.get(i)
  #     if (node == None):
  #       print("None, ", end='')
  #     while (node != None):
  #       print(node.get_value(),end='')
  #       node = node.get_next()
  #       if (node != None):
  #         print("->",end='')
  #       else:
  #         print(", ",end='')
  #   print("]")
  #   return