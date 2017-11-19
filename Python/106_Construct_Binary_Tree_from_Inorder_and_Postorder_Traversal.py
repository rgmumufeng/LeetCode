from leetcodelib import TreeNode, BinaryTree
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None
        
        tmp1 = zip(*sorted(enumerate(inorder), key=lambda x: x[1]))[0]
        tmp2 = zip(*sorted(enumerate(postorder), key=lambda x:x[1]))[0]
        post2in = zip(*sorted(zip(tmp2, tmp1)))[1]
        
        def rec(ini, inj, posti, postj):
            if inj-ini == 0 or postj-posti == 0:
                return None
            ind = post2in[postj-1]
            root = TreeNode(inorder[ind])
            root.left = rec(ini, ind, posti, posti+ind-ini)
            root.right = rec(ind+1, inj, posti+ind-ini, postj-1)
            return root
        return rec(0, len(inorder), 0, len(postorder))
    
    
class Solution2(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None
        
        tmp1 = zip(*sorted(enumerate(inorder), key=lambda x: x[1]))[0]
        tmp2 = zip(*sorted(enumerate(postorder), key=lambda x:x[1]))[0]
        post2in = list(zip(*sorted(zip(tmp2, tmp1)))[1])
        ref = zip(post2in, postorder)
        
        root = TreeNode(postorder.pop())
        ind = post2in.pop()
        i, j = 0, len(inorder)
        node, stack = root, []
        while True:
            if ind > i:
                stack.append((node, i, ind))
            if j > ind+1:
                node.right = TreeNode(postorder.pop())
                node = node.right
                i = ind+1
                ind = post2in.pop()
            elif stack:
                node, i, j = stack.pop()
                node.left = TreeNode(postorder.pop())
                node = node.left
                ind = post2in.pop()
            else:
                return root
            
            


if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    #nums = [2, 1, 3, 4, 7, 9, 10, 5, None, 6, 11, None, None, 12, 13, None, None, None, None, 14]
    nums = [1, 2]
    tree = BinaryTree(nums)
    arguments = [(tree.inorder(), tree.postorder())]
    answers = [nums]
    test(Solution2().buildTree, arguments, answers)
    #arguments = []
    #answers = []
    #test(Solution()., arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)