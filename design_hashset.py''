# -*- coding: utf-8 -*-
"""
Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

    add(value): Insert a value into the HashSet. 
    contains(value) : Return whether the value exists in the HashSet or not.
    remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.


Example:

MyHashSet hashSet = new MyHashSet();
hashSet.add(1);         
hashSet.add(2);         
hashSet.contains(1);    // returns true
hashSet.contains(3);    // returns false (not found)
hashSet.add(2);          
hashSet.contains(2);    // returns true
hashSet.remove(2);          
hashSet.contains(2);    // returns false (already removed)


Note:

    All values will be in the range of [0, 1000000].
    The number of operations will be in the range of [1, 10000].
    Please do not use the built-in HashSet library.
"""
class MyHashSet(object):
    NUM_BUCKETS = 10000
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._container = [[] for _ in range(self.NUM_BUCKETS)]
        
    def myhash(self, num):
        return num % self.NUM_BUCKETS

    def get_bucket(self, key):
        return self._container[self.myhash(key)]

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if self.contains(key):
            return

        self.get_bucket(key).append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if not self.contains(key):
            return
        bucket = self.get_bucket(key)
        bucket.pop(bucket.index(key))
        

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return key in self.get_bucket(key)
        

