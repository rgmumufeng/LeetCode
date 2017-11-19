from leetcodelib import TreeNode, BinaryTree
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        path = []
        self.rec(root, path)
        for i in xrange(len(path)-1):
            path[i].left = None
            path[i].right = path[i+1]
        return path[0]
    
    def rec(self, root, path):
        if not root:
            return
        path.append(root)
        self.rec(root.left, path)
        self.rec(root.right, path)
        
class Solution2(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.rec(root)
        return root
        
    
    def rec(self, root):
        if not root:
            return None
        
        left_end = self.rec(root.left)
        right_end = self.rec(root.right)
        
        if not left_end and not right_end:
            return root
        elif not left_end:
            return right_end
        elif not right_end:
            root.right, root.left = root.left, None
            return left_end
        else:
            left_end.right = root.right
            root.right, root.left = root.left, None
            return right_end
            
            
class Solution3(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.rec(root, None)
        return root
        
    def rec(self, root, prev):
        if not root:
            return prev
        prev = self.rec(root.right, prev)
        prev = self.rec(root.left, prev)
        root.right = prev
        root.left = None
        prev = root
        return prev

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    nums = [1,2,5,3,4,None,6]
    #nums = [1, 2]
    arguments = [BinaryTree(nums).root]
    answers = [sorted([x for x in nums if x != None])]
    test(Solution3().flatten, arguments, answers, mode='inorder')
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)