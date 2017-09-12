from leetcodelib import TreeNode, BinaryTree
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        elif p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    nums1 = [4, 2, 6, 1, 3, 5, 7]
    nums2 = [4, 2, 6, 1, None, 5, 7]
    nums3 = [4, 2, 6, None, 1, 5, 7] 
    
    tree1 = BinaryTree(nums1)
    tree2 = BinaryTree(nums2)
    tree3 = BinaryTree(nums3)
    
    arguments = [(tree1.root, tree1.root), (tree1.root, tree2.root), (tree2.root, tree3.root)]
    answers = [True, False, False]
    test(Solution().isSameTree, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)