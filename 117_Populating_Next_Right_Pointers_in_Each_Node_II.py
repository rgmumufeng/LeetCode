from leetcodelib import TreeNode, BinaryTree
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
        
    def __str__(self):
        left = self.left.val if self.left else None
        right = self.right.val if self.right else None
        return "Node: {}, left: {}, right: {}".format(self.val, left, right)

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        
        parent = root
        #dummy = TreeLinkNode(0)
        head = None
        while True:
            parent, head = self.find_next(parent)
            if not head:
                return write(root)
            node = head
            while node:
                if node == parent.left and parent.right:
                    node.next = parent.right
                else:
                    parent, next_node = self.find_next(parent.next)
                    node.next = next_node
                node = node.next
            parent = head
        return write(root)
            
    def find_next(self, parent):
        next_node = None
        while parent:
            if not parent.left and not parent.right:
                parent = parent.next
            else:
                next_node = parent.left if parent.left else parent.right
                break
        return parent, next_node
    
def write(root):
    path = []
    head = root
    while head:
        node = head
        while node:
            path.append(node.val)
            node = node.next
        parent, next_head = head, None
        while parent:
            if not parent.left and not parent.right:
                parent = parent.next
            else:
                next_head = parent.left if parent.left else parent.right
                break
        head = next_head
    return path

class Solution2:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        
        parent = root
        dummy = TreeLinkNode(0)
        child = dummy
        
        while parent:
            while parent:
                if parent.left:
                    child.next = parent.left
                    child = child.next
                if parent.right:
                    child.next = parent.right
                    child = child.next
                parent = parent.next
            parent = dummy.next
            child = dummy
            dummy.next = None
            
        return write(root)

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    m = 4
    n = 2**m -1
    nums = range(n)
    nodes = [TreeLinkNode(x) for x in nums]
    root = nodes[0]
    for i in xrange(n/2):
        nodes[i].left = nodes[2*i+1]
        nodes[i].right = nodes[2*(i+1)]
    
    nodes[2].left = None
    
    #print root, root.left, root.left.next, root.right
    arguments = [root]
    answers = [nums[:5]+nums[6:11]+nums[13:]]
    test(Solution2().connect, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)