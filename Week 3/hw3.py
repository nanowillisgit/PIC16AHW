#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Implementation of custom linked list class
Submission for homework 3

@author: Aatmun Baxi
@created: 10-27-20
"""
class Node:
    """Node class for storing data and next pointer for LinkedList class"""
    def __init__(self,dt):
        """Initializer for class, initializes data and 'pointer' to next node as None"""
        self.data = dt
        self.next = None

    def __str__(self):
        """Abstracts __str__ to work on Node object"""
        return str(self.data)

    def __repr__(self):
        """Abstracts __repr__ to work on Node object"""
        return repr(self.data)


class LinkedList:
    """Custom implementation of linked list object"""
    def __init__(self,dt):
        """Initializes linked list object with a single node containing dt

        Params
            dt (arbitrary type): data for first node to store
        """
        new = Node(dt)
        self.first = new
        self.last = new
        self.n = 1

    def append(self,dt):
        """Appends new node to list

        Params
            dt (arbitrary type): data for first node to store
        """
        new = Node(dt)
        self.last.next = new
        self.last = new
        self.n += 1

    # def __iter__(self):
        # self.index = 0
        # self.current = self.first
        # return self

    # def __next__(self):
        # if self.index == ( self.n ):
            # raise StopIteration
        # self.index = self.index + 1
        # to_return = self.current.data
        # self.current = self.current.next
        # return to_return

    def __iter__(self):
        """Iteration through linked list

        Returns
            Generator looping forward through list
        """
        return self.generator()

    def generator(self):
        """Generator for data stored in each node of list

        Returns
            (Node.data dtype) Yielded value in generator
        """
        self.current = self.first
        for i in range(0,self.n):
            # Thing to yield
            yld = self.current.data
            # Update current node for next generation
            self.current = self.current.next
            yield yld

    def __str__(self):
        """Gives string representation of linked list

        Returns
            (string) string of linked list
        """
        s = "["
        for a in self:
            s += str(a)
            s += "->"
        s += "]"
        return s


    def __repr__(self):
        """Gives representation of linked list

        Returns
            (string) representation of linked list
        """
        return f"'{str(self)}'"

    def __len__(self):
        """Abstracts len method for linked list

        Returns
            (int) length of list
        """
        return self.n

    def __getitem__(self, key):
        """Allows for random access of linked list nodes

        Params
            key (int): index to subscript linked list by

        Returns
            (Node.data dtype) value stored in the key-th node of linked list
        """
        ## TypeError if not an integer
        if not isinstance(key, int):
            raise TypeError(f'LinkedList cannot be indexed with {type(key)}')
        ## IndexError if out of bounds
        if key > (self.n - 1):
            raise IndexError('list index out of range')

        ## Return index of LinkedList
        curr = self.first
        for i in range(self.n):
            if i == key:
                return curr.data
            else:
                curr = curr.next

        #items = [i for i in self]
        #return items[key]

    def __setitem__(self, key, newval):
        """Random assignment

        Params
            key (int): index to subscript linked list by
            newval (arbitrary): new data to be assigned to
        """
        ## TypeError if not an integer
        if not isinstance(key, int):
            raise TypeError(f'LinkedList cannot be indexed with {type(key)}')
        ## IndexError if out of bounds
        if key > (self.n - 1):
            raise IndexError('Index out of bounds')

        ### Run through list and change key's data
        current = self.first
        for i in range(0, key):
            current = current.next
        current.data = newval

    def __add__(self, s):
        """Binary + operation of linked list with arbitrary data type

        Params
            s (arbitrary): new data to be added to list

        Returns
            (LinkedList) copy of self with appended data
        """
        ## Initialize copy of self
        copy = LinkedList(self.first.data)
        for i in range(1,self.n):
            copy.append(self[i])

        ## Append new data to copy and return
        copy.append(s)
        return copy
