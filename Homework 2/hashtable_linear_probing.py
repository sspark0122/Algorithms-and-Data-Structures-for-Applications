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
    # Raise exception if either key or value is None
    if (key == None or value == None):
      raise ValueError("Neither Key nor Value can be None")

    h = cs5112_hash1(key) % self.array_size

    # If nothing exists at this location, just insert, increment
    if self.array.get(h) == None:
      self.array.set(h, (key, value))
      self.item_count += 1
    else:
    # Iterate through the next elements until you reach a None, update if you see the same key
      while self.array.get(h) != None:
        if self.array.get(h)[0] == key:
          self.array.set(h, (key,value))
          return
        h = (h + 1) % self.array_size

      # Insert value at this None
      self.array.set(h, (key, value))
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

    h = cs5112_hash1(key) % self.array_size
    
    if self.array.get(h) == None:
      return None
  
    while self.array.get(h) != None:
      if self.array.get(h)[0] == key:
        return self.array.get(h)[1]
      h = (h + 1) % self.array_size
      
    return None

  # Removes the `(key, value)` pair matching the given `key` from the map, if it
  # exists. If such a pair exists in the map, the return value will be the value
  # that was removed. If no such value exists, the method will return None.
  # Note: `key` may not be None (an exception will be raised)
  def remove(self, key):
    # If key is None, raise an Exception
    if (key == None):
      raise ValueError("Key can't be None")

    h = cs5112_hash1(key) % self.array_size
    result = None
    
    # If None at that hash table value can return immedietely
    if self.array.get(h) == None:
      return None
  
    # Iterate through array to check for key matches  
    while self.array.get(h) != None:
      if self.array.get(h)[0] == key:
        result = self.array.get(h)[1]
        self.array.set(h, None)
        self.item_count -= 1
        break
      h = (h + 1) % self.array_size
    
    # If result is found, need to reinsert next
    if result != None: 
      tupList = []
      curr = (h + 1) % self.array_size
      
      while (self.array.get(curr) != None):
        tupList.append(self.array.get(curr))
        self.array.set(curr, None)
        self.item_count -= 1
        curr = (curr + 1) % self.array_size

      for (k,v) in tupList:
        self.insert(k,v)
    
    return result

  # Returns the number of elements in the hash table.
  def size(self):
    # YOUR CODE HERE
    return self.item_count

  # Internal helper function for resizing the hash table's array once the ratio
  # of stored mappings to array size exceeds the specified load factor.
  def _resize_array(self):
    # YOUR CODE HERE    
    self.array_size *= 2
    oldArray = self.array
    self.array = FixedSizeArray(self.array_size)
        
    for i in range(0, oldArray.size):
      if oldArray.get(i) != None:  
        h = cs5112_hash1(oldArray.get(i)[0]) % self.array_size
      
        while self.array.get(h) is not None:
          h = (h + 1) % self.array_size
      
        self.array.set(h, (oldArray.get(i)[0], oldArray.get(i)[1]))

  # Internal helper function for accessing the array underlying the hash table.
  def _get_array(self):
    # DO NOT EDIT THIS METHOD
    return self.array

  # def printArray(self):
  #   print("[", end = '')
  #   for i in range(self.array_size):
  #     print(str(self.array.get(i))+", ", end = '')
  #   print("]")
  #   return