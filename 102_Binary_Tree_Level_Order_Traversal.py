from leetcodelib import TreeNode, BinaryTree
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        level, ans = [root], []
        while level:
            tmp, values = [], []
            for node in level:
                values.append(node.val)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            ans.append(values)
            level = tmp
        return ans
            
        
        
if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    nums = [[3,9,20,None,None,15,7]]
    arguments = [BinaryTree(x).root for x in nums]
    answers = [[[3],[9,20],[15,7]]]
    test(Solution().levelOrder, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)