from leetcodelib import TreeNode, BinaryTree
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.path = self.mostleft(root)
        
    def mostleft(self, node):
        stack = []
        while node:
            stack.append(node)
            node = node.left
        return stack
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.path else False
        

    def next(self):
        """
        :rtype: int
        """
        node = self.path.pop()
        self.path.extend(self.mostleft(node.right))
        return node.val
        

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    #arguments = []
    #answers = []
    #test(Solution()., arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)