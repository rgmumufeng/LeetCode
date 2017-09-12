from leetcodelib import BinaryTree
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.rec(root, root)
    
    
    def rec(self, root1, root2):
        if not root1 and not root2:
            return True
        
        if root1 and root2:
            return root1.val == root2.val and self.rec(root1.left, root2.right) and self.rec(root1.right, root2.left)
        
        return False

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    nums = [[1, 2, 2, 3, 4, 4, 3], [1, 2, 2, None, 3, None, 3]]
    
    arguments = [BinaryTree(x).root for x in nums]
    answers = [True, False]
    test(Solution().isSymmetric, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)