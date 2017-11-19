from leetcodelib import TreeNode
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        node, stack = root, []
        while node or stack:
            if node:
                if node.right:
                    stack.append(node.right)
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if stack and node.right == stack[-1]:
                    tmp, node = node, stack.pop()
                    stack.append(tmp)
                else:
                    res.append(node.val)
                    node = None
        return res
                
                    

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    #arguments = []
    #answers = []
    #test(Solution()., arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)