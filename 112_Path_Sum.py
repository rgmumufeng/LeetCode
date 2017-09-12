from leetcodelib import TreeNode, BinaryTree
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right:
            return True if root.val == sum else False
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)
    
if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    nums = [5,4,8,11,None,13,4,7,2,None,None,None,1]
    arguments = [(BinaryTree(nums).root, 22)]
    answers = [True]
    test(Solution().hasPathSum, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)