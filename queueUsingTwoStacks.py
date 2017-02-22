#!/usr/bin/env python2

"""
I took this challenge in HackerRank. It was not too challenging, but I liked the idea of using two stacks to make a queue.
In the code I have implemented both queue types: one using a python list, and another using two python lists treated like stacks.

From HackerRank:
A queue is an abstract data type that maintains the order in which elements were added to it, allowing the oldest elements to be removed from the front and new elements to be added to the rear. This is called a First-In-First-Out (FIFO) data structure because the first element added to the queue (i.e., the one that has been waiting the longest) is always the first one to be removed.
In this challenge, you must first implement a queue using two stacks.
"""

class simpleQueue(object):
    def __init__(self):
        self.q = []
        
    def peek(self):
        return self.q[0]
        
    def pop(self):
        return self.q.pop(0)
        
    def put(self, value):
        self.q.append(value)

    def isEmpty(self):
        return len(self.q) == 0
        

class stacksQueue(object):
    def __init__(self):
        self.first = []
        self.second = []
        
    def peek(self):
        try:
            return self.second[-1]
        except IndexError:
            self.moveFirstToSecond()
        # We don't control errors when peeking in an empty queue.
        # That is the user's responsibility! (using isEmpty)
        return self.second[-1]
        
    def pop(self):
        try:
            return self.second.pop()
        except IndexError:
            self.moveFirstToSecond()
        # We don't control errors when popping from an empty queue.
        # That is the user's responsibility! (using isEmpty)
        return self.second.pop()

    def put(self, value):
        self.first.append(value)

    def moveFirstToSecond(self):
        # Moves all elements from the first stack to the (empty) second stack
        while len(self.first) > 0:
            self.second.append(self.first.pop())

    def isEmpty(self):
        return len(self.first) == 0 and len(self.second) == 0
