from leetcodelib import BinaryTree
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        level, ans, direction = [root], [], -1
        while level:
            tmp, values = [], []
            for i in xrange(len(level)):
                values.append(level[i].val)
                children = [level[~i].left, level[~i].right]
                for child in children[::direction]:
                    if child:
                        tmp.append(child)
            ans.append(values)
            level = tmp
            direction = -direction
        return ans

                

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    nums = [[3,9,20,None,None,15,7], [1,2,3,4,None,None,5]]
    arguments = [BinaryTree(x).root for x in nums]
    answers = [[[3],[20,9],[15,7]], [[1], [3, 2], [4, 5]]]
    test(Solution().zigzagLevelOrder, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)