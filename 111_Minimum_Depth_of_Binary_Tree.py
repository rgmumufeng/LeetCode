from leetcodelib import TreeNode, BinaryTree
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        dep = float('inf')
        level = [root]
        count = 1
        while level:
            tmp, updated = [], False
            for node in level:
                if (not updated) and (not node.left) and (not node.right):
                    dep = min(dep, count)
                    updated = True
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            level = tmp
            count += 1
        return dep
    
    
class Solution2(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left * right: 
            return min(left, right)+1
        else:
            return max(left, right)+1

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    nums = [[4,2,6,1,3,5,7], [5,4,6,3,None,None,7], [5,4,6,3,None,None,7,None,None,None,8], [5,4,6,3,None,None,7,2]]
    arguments = [BinaryTree(x).root for x in nums]
    answers = [3, 3, 3, 3]
    test(Solution2().minDepth, arguments, answers, inds=None)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)