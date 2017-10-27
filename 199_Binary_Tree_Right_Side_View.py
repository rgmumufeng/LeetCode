from leetcodelib import TreeNode, BinaryTree
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        res, level = [], [root]
        while level:
            res.append(level[-1].val)
            level = [node for parent in level for node in (parent.left, parent.right) if node]
        return res
            
        

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    nums = [1]
    arguments = [BinaryTree(nums).root]
    answers = [[1]]
    test(Solution().rightSideView, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)