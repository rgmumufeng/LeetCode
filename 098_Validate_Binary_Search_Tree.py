from leetcodelib import TreeNode, BinaryTree

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.rec(root, [])
    
    def rec(self, root, ans):
        if not root:
            return True
        if not self.rec(root.left, ans):
            return False
        if ans and root.val <= ans[-1]:
            return False
        else:
            ans.append(root.val)
            return self.rec(root.right, ans)
        
class Solution2(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.rec(root)
    
    def rec(self, root, minval=-float('inf'), maxval=float('inf')):
        if not root:
            return True
        if root.val <= minval or root.val >= maxval:
            return False
        return self.rec(root.left, minval, root.val) and self.rec(root.right, root.val, maxval)
        
        
        
if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    nums = [[4, 2, 6, 1, 3, 5, 7],
            [4, 2, 5, 3, 1, 6, 7],
            [4, 2, 5, 1, 3, 7, 6],
            [10, 5, 15, None, None, 6, 20]]
    
    arguments = [BinaryTree(nums).root for nums in nums]
    answers = [True, False, False, False]
    test(Solution2().isValidBST, arguments, answers, inds=None)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)