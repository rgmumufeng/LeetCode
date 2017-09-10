from leetcodelib import TreeNode, BinaryTree
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        #return self.rec(1, n+1)
        ans = self.rec(1, n+1)
        #for a in ans:
        #    print BinaryTree(a).values()
        return len(ans)
    
    def rec(self, i, j):
        if j-i == 0:
            return [None]
        
        ans = []
        for x in xrange(i, j):
            for left in self.rec(i, x):
                for right in self.rec(x+1, j):
                    root = TreeNode(x)
                    root.left, root.right = left, right
                    ans.append(root)
        return ans
        
if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [3, 4, 5, 6]
    answers = [5, 14,42, 132]
    test(Solution().generateTrees, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)