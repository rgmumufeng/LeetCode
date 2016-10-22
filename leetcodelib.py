'''
Created on Aug 17, 2016
@author: Bo Xu
BinaryTree serialization, deserialization method is borrowed from StefanPochmann with modifications
(https://discuss.leetcode.com/topic/16600/tree-deserializer-and-visualizer-for-python)
'''

import time
import numpy as np
from collections import deque, Sequence


def test(method, arguments, answers):
    start_time = time.time()
    for i, arg in enumerate(arguments):
        if isinstance(arg, Sequence) and not isinstance(arg, basestring):
            args = arg
        else:
            args = (arg,)
        result = method(*args)
        if result != answers[i]:
            print "{}: {} != {}".format(i, result, answers[i])
    print("Tests finished in %s seconds" % (time.time() - start_time))
    

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

        
class LinkedList(object):
    def __init__(self, inputs=[]):
        if isinstance(inputs, ListNode):
            self.head = inputs
        elif len(inputs) == 0:
            self.head = None
        else:
            self.load(inputs)

    def load(self, numbers):
        node = dummy = ListNode(None)
        for x in numbers:
            node.next = ListNode(x)
            node = node.next
        self.head = dummy.next
        
    def values(self, head=None):
        if not head:
            head = self.head
            
        numbers = []
        while head:
            numbers.append(head.val)
            head = head.next
        return numbers
    
    def write(self, head=None):
        for x in self.values(head):
            print x,
        print

           
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        

class BinaryTree(object):
    def __init__(self, inputs=[]):
        if isinstance(inputs, TreeNode):
            self.root = inputs
        elif len(inputs) == 0:
            self.root = None
        else:
            self.load(inputs)
        
    def load(self, numbers):
        self.root = self.deserialization(numbers)

    def deserialization(self, numbers):
        nodes = [None if x == None else TreeNode(int(x)) for x in numbers]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left  = kids.pop()
                if kids: node.right = kids.pop()
        return root
    
    def values(self, root=None):
        if not root:
            root = self.root
        return self.serialization(root)
    
    def serialization(self, root):
        nodes = deque([root])
        numbers = []
        while nodes:
            node = nodes.popleft()
            if node:
                nodes.append(node.left)
                nodes.append(node.right)
                numbers.append(node.val)
            else:
                numbers.append(None)
                
        while numbers[-1] == None:
            numbers.pop()
        return numbers
        
    def write(self, root=None):
        for x in self.values(root):
            print x,
        print      


    

    