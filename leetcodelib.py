'''
Created on Aug 17, 2016
@author: Bo Xu
BinaryTree serialization, deserialization method is borrowed from StefanPochmann with modifications
(https://discuss.leetcode.com/topic/16600/tree-deserializer-and-visualizer-for-python)
'''

import yaml
import os
import time
from collections import deque

def  test(method, arguments, answers):
    start_time = time.time()
    for i, arg in enumerate(arguments):
        if isinstance(arg, tuple):
            args = arg
        else:
            args = (arg,)
        result = method(*args)
        if result == answers[i]:
            print "Case {} passed ...".format(i)
        else:
            print "Case {}: {} != {}".format(i, result, answers[i])
    print("%d tests finished in %s seconds" % (len(arguments), time.time() - start_time))


def update_testfile(testfile, arg_names, arguments, answers):
    arg_orders = arg_names.split(', ')
    if os.path.isfile(testfile):
        with open(testfile, 'r') as f:
            data = yaml.safe_load(f)
            if data[0]['argument_orders'] != arg_orders:
                raise ValueError('Input arguments order is not consistent with records!')
            test_cases = data[1:]
    else:
        test_cases = []
    
    saved_arguments = [tuple([x['input_args'][name] for name in arg_orders]) for x in test_cases]
    update_file = False
    for i, input_args in enumerate(arguments):
        if input_args not in saved_arguments:
            print "Adding new test case ..."
            test_cases.append({'input_args': dict(zip(arg_orders, input_args)), 'output_answer': answers[i]})
            update_file = True
    
    if update_file:        
        for i, case in enumerate(test_cases):
            case['case_number'] = i
        stream = yaml.safe_dump([dict(argument_orders=arg_orders)] + test_cases, indent=4)
        stream = stream.replace('\n- ', '\n\n- ')
        with open(testfile, 'w') as f:
            f.write(stream)
        print "File is updated."
    else:
        print "Nothing to update. Original file is kept"
    

def run_testfile(testfile, method, inds=None):
    with open(testfile, 'r') as f:
        data = yaml.safe_load(f)
        arg_orders = data[0]['argument_orders']
        test_cases = data[1:]
    
    if isinstance(inds, int):
        n = min(inds, len(test_cases))
        test_cases = test_cases[:n]
    elif isinstance(inds, (list, tuple)):
        n = len(inds)
        test_cases = [test_cases[i] for i in inds]
    elif inds == None:
        n = len(test_cases)
    else:
        raise ValueError("Invalid arguments 'inds': {}".format(inds))
    
    start_time = time.time()
    for case in test_cases:
        args = tuple([case['input_args'][name] for name in arg_orders])
        result = method(*args)
        if result == case['output_answer']:
            print "Case {} passed ...".format(case['case_number'])
        else:
            print "Case {}: {} != {}".format(case['case_number'], result, case['output_answer'])
    print("%d tests finished in %s seconds" % (n, time.time() - start_time))


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
    def __repr__(self):
        return "ListNode %s" % str(self.val)

        
class LinkedList(object):
    def __init__(self, inputs=[]):
        if isinstance(inputs, ListNode):
            self.head = inputs
        elif len(inputs) == 0:
            self.head = None
        else:
            self.load(inputs)
            
    def __repr__(self):
        s = "->".join([str(x) for x in self.values()])
        return "LinkedList %s" % s

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


    

    