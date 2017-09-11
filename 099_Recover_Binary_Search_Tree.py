from leetcodelib import TreeNode, BinaryTree
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        tmp = [TreeNode(-float('inf')), None, None]
        self.rec(root, tmp)
        tmp[1].val, tmp[2].val = tmp[2].val, tmp[1].val
        return BinaryTree(root).inorder()
        
    def rec(self, root, tmp):
        if root:
            self.rec(root.left, tmp)
            if tmp[0].val >= root.val:
                if not tmp[1]:
                    tmp[1] = tmp[0]
                tmp[2] = root
            tmp[0] = root
            self.rec(root.right, tmp)

            
class Solution2(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
                 
if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    nums = [[4, 2, 7, 1, 3, 5, 6]]
    arguments = [BinaryTree(num).root for num in nums]
    answers = [sorted(num) for num in nums]
    
    test(Solution().recoverTree, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)