from leetcodelib import TreeNode, BinaryTree
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        height, node = 1, root
        while node.right:
            node = node.right
            height += 1
        count = 2 ** height - 1
        #print count
        
        node, h, stack = root, 1, []
        while node or stack:
            if node:
                if node.right:
                    stack.append((node.right, h+1))
                stack.append((node, h))
                node, h = node.left, h+1
            else:
                node, h = stack.pop()
                if stack and node.right == stack[-1][0]:
                    stack.pop()
                    stack.append((node, h))
                    node, h = node.right, h+1
                else:
                    #print "tree", node.val, 'height', h
                    if h > height:
                        count += 1
                    elif not node.right:
                        return count
                    node, h = None, None
                    #print count
        return count
                    

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    tree1 = BinaryTree([1, 2, 3, 4, 5])
    arguments = [tree1.root]
    answers = [5]
    test(Solution().countNodes, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)