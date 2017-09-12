from leetcodelib import BinaryTree
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1
    
class Solution2(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        level, count = [root], 1
        while level:
            tmp = []
            for node in level:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            if not tmp:
                break
            level = tmp
            count +=1
        return count
        
        

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    nums = [[3,9,20,None,None,15,7], [1,2,3,4,None,None,5]]
    arguments = [BinaryTree(x).root for x in nums]
    answers = [3, 3]
    test(Solution2().maxDepth, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)