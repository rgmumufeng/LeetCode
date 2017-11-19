from leetcodelib import TreeNode, BinaryTree
class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        node, stack = root, []
        while node.left:
            stack.append(node)
            node = node.left
        
        newroot = node
        while stack:
            parent = stack.pop()
            node.left, node.right = parent.right, parent
            parent.right = None
            node = parent
        node.left = None
        return newroot

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    nums = [[1, 2]]
    arguments = [BinaryTree(x).root for x in nums]
    answers = [[2, None, 1]]
    test(Solution().upsideDownBinaryTree, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)