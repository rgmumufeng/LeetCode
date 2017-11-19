from leetcodelib import TreeNode, BinaryTree
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder and not inorder:
            return None
        for i in xrange(len(inorder)):
            if inorder[i] == preorder[0]:
                break
        root = TreeNode(preorder[0])
        root.left = self.buildTree(preorder[1:i+1], inorder[:i])
        root.right = self.buildTree(preorder[i+1:], inorder[i+1:])
        return root
    

class Solution2(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder and not inorder:
            return None
        tmp1 = zip(*sorted(enumerate(preorder), key=lambda x: x[1]))[0]
        tmp2 = zip(*sorted(enumerate(inorder), key=lambda x:x[1]))[0]
        pre2in = zip(*sorted(zip(tmp1, tmp2)))[1]
        
        def rec(prei, prej, ini, inj):
            if prej==prei and inj==ini:
                return None
            ind = pre2in[prei]
            root = TreeNode(preorder[prei])
            root.left = rec(prei+1, prei+1+ind-ini, ini, ind)
            root.right = rec(prei+1+ind-ini, prej, ind+1, inj)
            return root
            
        return rec(0, len(preorder), 0, len(inorder))
    
    
class Solution3(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder and not inorder:
            return None
        
        tmp1 = zip(*sorted(enumerate(preorder), key=lambda x: x[1]))[0]
        tmp2 = zip(*sorted(enumerate(inorder), key=lambda x:x[1]))[0]
        pre2in = zip(*sorted(zip(tmp1, tmp2)))[1]
                
        root = TreeNode(preorder[0])
        i, j, k = 0, len(inorder), 0
        node, stack = root, []
        while True:
            ind = pre2in[k]
            if j-ind-1 > 0:
                stack.append((node, ind+1, j))
            if ind-i > 0:
                k += 1
                node.left = TreeNode(preorder[k])
                node = node.left
                j = ind
            elif stack:
                node, i, j = stack.pop()
                k += 1
                node.right = TreeNode(preorder[k])
                node = node.right
            else:
                return root
                

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    #nums = [2, 1, 3, 4, 7, 9, 10, 5, None, 6, 11, None, None, 12, 13, None, None, None, None, 14]
    nums = [1, None, 2]
    tree = BinaryTree(nums)
    arguments = [(tree.preorder(), tree.inorder())]
    answers = [nums]
    test(Solution3().buildTree, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)