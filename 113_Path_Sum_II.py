from leetcodelib import BinaryTree
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        if not root.left and not root.right:
            return [[root.val]] if root.val == sum else []
        
        return [[root.val]+p for p in self.pathSum(root.left, sum-root.val)+self.pathSum(root.right, sum-root.val)]
             

class Solution2(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ans = []
        node, stack, tot, path = root, [], 0, []
        while node or stack:
            if node:
                tot += node.val
                path.append(node.val)
                if not node.left and not node.right:
                    if tot == sum:
                        ans.append(path)
                    node = None
                else:
                    if node.right:
                        stack.append((tot, node.right, list(path)))
                    node = node.left
            else:
                tot, node, path = stack.pop()
        return ans
                
                
                
                
                
        

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    nums = [5,4,8,11,None,13,4,7,2,None,None,5,1]
    arguments = [(BinaryTree(nums).root, 22)]
    answers = [[[5,4,11,2],[5,8,4,5]]]
    test(Solution2().pathSum, arguments, answers, mode='1D')
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)