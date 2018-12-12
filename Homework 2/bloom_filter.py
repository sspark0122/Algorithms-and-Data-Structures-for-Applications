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
from cs5112_hash import cs5112_hash2
from cs5112_hash import cs5112_hash3

# Implementation of a basic bloom filter. Uses exactly three hash functions.
class BloomFilter:
  def __init__(self, size=10):
    # DO NOT EDIT THIS CONSTRUCTOR
    self.size = size
    self.array = FixedSizeArray(size)
    for i in range(0, size):
      self.array.set(i, False)

  # Adds an element to the bloom filter using three hash functions.
  def add_elem(self, elem):
    # If elem is None, raise an Exception
    if (elem == None):
      raise ValueError("Key can't be None")
    # Calculate the hashes for a given element.
    h1 = cs5112_hash1(elem) % self.size
    h2 = cs5112_hash2(elem) % self.size
    h3 = cs5112_hash3(elem) % self.size
    
    # Set True at h1, h2, and h3.
    self.array.set(h1, True)
    self.array.set(h2, True)
    self.array.set(h3, True)

  # Returns False if the given element was definitely not added to the
  # filter. Returns True if it's possible that the element was added to the
  # filter (but not necessarily certain).
  def check_membership(self, elem):
    # If elem is None, raise an Exception
    if (elem == None):
      raise ValueError("Key can't be None")
    # Calculate the hashes for a given element.
    h1 = cs5112_hash1(elem) % self.size
    h2 = cs5112_hash2(elem) % self.size
    h3 = cs5112_hash3(elem) % self.size
    
    return (self.array.get(h1) and self.array.get(h2) and self.array.get(h3))
        
