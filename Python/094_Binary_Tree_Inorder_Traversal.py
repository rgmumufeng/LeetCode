from leetcodelib import TreeNode, BinaryTree
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        #self.rec(root, ans)
        self.ite(root, ans)
        return ans
        
    def rec(self, root, ans):
        if not root:
            return []
        self.rec(root.left, ans)
        ans.append(root.val)
        self.rec(root.right, ans)
        
    def ite(self, root, ans):
        node, stack = root, []
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                ans.append(node.val)
                node = node.right
        return ans

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    from random import sample
    nums = [2, 1, 3, 0, 7, 9, 1, 2, None, 1, 0, None, None, 8, 8, None, None, None, None, 7]
    tree = BinaryTree(nums)
    arguments = [tree.root]
    answers = [tree.inorder()]
    test(Solution().inorderTraversal, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)