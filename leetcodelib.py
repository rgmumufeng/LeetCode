'''
Created on Aug 17, 2016
@author: Bo Xu
BinaryTree serialization, deserialization method is borrowed from StefanPochmann with modifications
(https://discuss.leetcode.com/topic/16600/tree-deserializer-and-visualizer-for-python)
'''

import os, time, yaml
from collections import deque

def test(method, arguments, answers, inds=None):
    if inds == None:
        inds = range(len(arguments))
    elif isinstance(inds, int):
        inds = range(min(inds, len(arguments)))
    elif not isinstance(inds, (list, tuple)):
        raise ValueError("Invalid argument 'inds': {}".format(inds))
    
    start_time = time.time()
    for i in inds:
        if isinstance(arguments[i], tuple):
            args = arguments[i]
        else:
            args = (arguments[i],)
        result = method(*args)
        if result == answers[i]:
            print "Case {} passed ...".format(i)
        else:
            print "Case {} did NOT pass !!!\nresult: {}\nanswer: {}".format(i, result, answers[i])
    print("%d tests finished in %s seconds\n" % (len(inds), time.time() - start_time))


def load_testfile(testfile):
    if os.path.isfile(testfile):
        with open(testfile, 'r') as f:
            data = yaml.safe_load(f)
            arg_orders = data[0]['argument_orders']
            test_cases = data[1:]
        arguments = [tuple([x['input_args'][name] for name in arg_orders]) for x in test_cases]
        answers = [x['output_answer'] for x in test_cases]
        return arg_orders, arguments, answers
    else:
        return [], [], []


def update_testfile(testfile, arg_names, arguments, answers, inds=None):
    if inds == None:
        inds = range(len(arguments))
    elif isinstance(inds, int):
        inds = range(min(inds, len(arguments)))
    elif not isinstance(inds, (list, tuple)):
        raise ValueError("Invalid arguments 'inds': {}".format(inds))
    
    saved_arg_orders, saved_arguments, saved_answers = load_testfile(testfile)
    arg_orders = arg_names.split(', ')
    if saved_arg_orders and saved_arg_orders != arg_orders:
        raise ValueError("Argument names mismatch!")
    print "%d test cases in total." % len(saved_arguments)
    
    new_cases = []
    for i in inds:
        if isinstance(arguments[i], tuple):
            input_args = arguments[i]
        else:
            input_args = (arguments[i],)
        if input_args not in saved_arguments:
            case = {'case_number': len(saved_arguments) + len(new_cases),
                    'input_args': dict(zip(arg_orders, input_args)), 
                    'output_answer': answers[i]}
            new_cases.append(case)
            print "New case added. %d test cases in total." % (len(saved_arguments)+len(new_cases))
    
    if new_cases:
        with open(testfile, 'a') as f:
            if len(saved_arguments) == 0:
                yaml.safe_dump([{'argument_orders': arg_orders}], f)
            stream = yaml.safe_dump(new_cases, indent=4)
            stream = '\n' + stream.replace('\n- ', '\n\n- ')
            f.write(stream)
        print "File is updated."
    else:
        print "Nothing to update. Original file is kept"
        

def run_testfile(testfile, method, inds=None):
    arg_orders, arguments, answers = load_testfile(testfile)
    test(method, arguments, answers, inds)
    return


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


    

    