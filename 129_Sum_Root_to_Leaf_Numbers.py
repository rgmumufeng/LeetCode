from leetcodelib import TreeNode, BinaryTree
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        node, stack, tot = root, [], 0
        while node or stack:
            if node:
                tot = tot*10+node.val
                if not node.left and not node.right:
                    res += tot
                elif node.right:
                    stack.append((node.right, tot))
                node = node.left
            else:
                node, tot = stack.pop()
        return res
                    
                           
class Solution2(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.rec(root, 0)
        return self.res
        
    def rec(self, root, tot):
        if root:
            self.rec(root.left, tot*10+root.val)
            self.rec(root.right, tot*10+root.val)
            if not root.left and not root.right:
                self.res += tot*10+root.val
                
                
            

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    nums = [[1, 2, 3], [1, None, 5], [1, 5, None]]
    arguments = [BinaryTree(x).root for x in nums]
    answers = [25, 15, 15]
    test(Solution().sumNumbers, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)