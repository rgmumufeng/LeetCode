from leetcodelib import TreeNode, BinaryTree
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        mid = len(nums)/2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
        

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [range(100)]
    answers = [x for x in arguments]
    test(Solution().sortedArrayToBST, arguments, answers, mode='inorder')
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)