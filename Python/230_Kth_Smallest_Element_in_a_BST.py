from leetcodelib import TreeNode, BinaryTree
class Solution2(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root or k == 0:
            return None
        node, stack = root, []
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                k -= 1
                if k == 0:
                    return node.val
                node = node.right
                

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    nums = [[1, None, 2], [3, 1, 4, None, 2]]
    ks = [2, 2]
    arguments = [(BinaryTree(nums[i]).root, ks[i]) for i in xrange(len(ks))]
    answers = [2, 2]
    test(Solution().kthSmallest, arguments, answers, inds=[1])
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)