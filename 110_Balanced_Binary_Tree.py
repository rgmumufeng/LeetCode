from leetcodelib import TreeNode, BinaryTree
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return True if self.calculate(root) >= 0 else False
        
    def calculate(self, root):
        if not root:
            return 0
        hleft = self.calculate(root.left)
        if hleft == -1:
            return -1
        hright = self.calculate(root.right)
        if hright == -1:
            return -1
        if -1 <= hleft - hright <= 1:
            return max(hleft, hright)+1
        else:
            return -1
        

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    nums = [[4,2,6,1,3,5,7], [5,4,6,3,None,None,7], [5,4,6,3,None,None,7,None,None,None,8]]
    arguments = [BinaryTree(x).root for x in nums]
    answers = [True, True, False]
    test(Solution().isBalanced, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)