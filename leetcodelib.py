'''
Created on Aug 17, 2016
@author: Bo Xu
BinaryTree serialization, deserialization method is borrowed from StefanPochmann with modifications
(https://discuss.leetcode.com/topic/16600/tree-deserializer-and-visualizer-for-python)
'''

import os, time, yaml
from collections import deque


def transfer(a, b, mode):
    if mode == 'direct':
        return a, b
    
    elif isinstance(a, ListNode) or isinstance(b, ListNode):
        return LinkedList(a).values(), LinkedList(b).values()
    
    elif mode == '1D':
        return sorted(a), sorted(b)
    
    elif mode == '2D':
        return sorted([sorted(x) for x in a]), sorted([sorted(x) for x in b])

    else:
        return a, b
    

def test(method, arguments, answers, inds=None, mode=None):
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
        result, answer = transfer(result, answers[i], mode)
        if result == answer:
            print "Case {} passed ...".format(i)
        else:
            print "Case {} did NOT pass !!!\nresult: {}\nanswer: {}".format(i, result, answer)
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
        raise ValueError("File does not exist!")
    

def generate_testfile_stream(arg_orders, arguments, answers, num_existed=0):
    new_cases = []
    for i in xrange(len(arguments)):
        if isinstance(arguments[i], tuple):
            input_args = arguments[i]
        else:
            input_args = (arguments[i],)
        
        if len(input_args) != len(arg_orders):
            raise ValueError("Wrong arguments for case {}".format(i))
        
        case = {'case_number': i + num_existed,
                'input_args': dict(zip(arg_orders, input_args)), 
                'output_answer': answers[i]}
        new_cases.append(case)

    stream = yaml.safe_dump(new_cases, indent=4)
    stream = '\n' + stream.replace('\n- ', '\n\n- ')
    return stream


def update_testfile(testfile, arg_names, arguments, answers, mode='generate', inds=None):
    '''
    mode: 'generate': generate new
          'add': append to existed
    '''
    if len(arguments) != len(answers):
        raise ValueError("Length of arguments and answers mismatch!")
    
    if inds == None:
        inds = range(len(arguments))
    elif isinstance(inds, int):
        inds = range(min(inds, len(arguments)))
    elif not isinstance(inds, (list, tuple)):
        raise ValueError("Invalid arguments 'inds': {}".format(inds))
    
    if len(inds) <= 0:
        print "Nothing to update. Original file is kept (if existed)."
        return
        
    arg_orders = arg_names.split(', ')
    new_arguments = [arguments[i] for i in inds]
    new_answers = [answers[i] for i in inds]
    
    if mode == "generate":
        with open(testfile, 'w') as f:
            yaml.safe_dump([{'argument_orders': arg_orders}], f)
        num_existed = 0
    elif mode == "add":
        saved_arg_orders, saved_arguments, _ = load_testfile(testfile)
        if saved_arg_orders != arg_orders:
            raise ValueError("New argument names are different from saved ones!")
        num_existed = len(saved_arguments)
    else:
        raise ValueError("Invalid mode. Should be 'generate' or 'add'.")
    
    with open(testfile, 'a') as f:
        print "%d test cases existed." % num_existed
        stream = generate_testfile_stream(arg_orders, new_arguments, new_answers, num_existed)
        #print stream
        print "%d new test cases added." % len(new_arguments)
        f.write(stream)
        print "File is updated."


def run_testfile(testfile, method, inds=None):
    _, arguments, answers = load_testfile(testfile)
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
        
    def inorder(self, root=None):
        def helper(node, values):
            if node:
                helper(node.left, values)
                values.append(node.val)
                helper(node.right, values)
        if not root:
            root = self.root
        values = []
        helper(root, values)
        return values
    
    def preorder(self, root=None):
        def helper(node, values):
            if node:
                values.append(node.val)
                helper(node.left, values)
                helper(node.right, values)
        if not root:
            root = self.root
        values = []
        helper(root, values)
        return values
    
    def postorder(self, root=None):
        def helper(node, values):
            if node:
                helper(node.left, values)
                helper(node.right, values)
                values.append(node.val)
        if not root:
            root = self.root
        values = []
        helper(root, values)
        return values
    
    
    def morris_inorder(self, root=None):
        if not root:
            root = self.root
        node, values = root, []
        while node:
            if not node.left:
                values.append(node.val)
                node = node.right
            else:
                tmp = node.left
                while tmp.right and tmp.right != node:
                    tmp = tmp.right
                if not tmp.right:
                    tmp.right = node
                    node = node.left
                else:
                    tmp.right = None
                    values.append(node.val)
                    node = node.right
        return values
    
    def morris_preorder(self, root=None):
        if not root:
            root = self.root
        node, values = root, []
        while node:
            if not node.left:
                values.append(node.val)
                node = node.right
            else:
                tmp = node.left
                while tmp.right and tmp.right != node:
                    tmp = tmp.right
                if not tmp.right:
                    tmp.right = node
                    values.append(node.val)
                    node = node.left
                else:
                    tmp.right = None
                    node = node.right
        return values
                    
                    
                

