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
        if not root or not root.left:
            return
        
        head = root
        dummy = TreeLinkNode(None)
        while head.left:
            parent = head
            node = dummy
            while parent:
                node.next = parent.left
                parent.left.next = parent.right
                node = parent.right
                parent = parent.next
            head = head.left
        return write(root)
            
def write(root):
    path = []
    head = root
    while head:
        node = head
        while node:
            path.append(node.val)
            node = node.next
        head = head.left
    return path

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    m = 10
    n = 2**m -1
    nums = range(n)
    nodes = [TreeLinkNode(x) for x in nums]
    root = nodes[0]
    for i in xrange(n/2):
        nodes[i].left = nodes[2*i+1]
        nodes[i].right = nodes[2*(i+1)]

    #for i in xrange(1, m):
    #    j = (2**i)-1
    #    for x in xrange(j):
    #        nodes[j+x].next = nodes[j+x+1]
    #print write(root)
    
    arguments = [root]
    answers = [nums]
    test(Solution().connect, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)