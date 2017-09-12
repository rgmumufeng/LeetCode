from leetcodelib import TreeNode, BinaryTree
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        level = [root]
        path = []
        while level:
            tmp, values = [], []
            for node in level:
                values.append(node.val)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            path.append(values)
            level = tmp
        return path[::-1]    

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    nums = [3,9,20,None,None,15,7]    
    arguments = [BinaryTree(nums).root]
    answers = [[[15,7],[9,20],[3]]]
    test(Solution().levelOrderBottom, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)