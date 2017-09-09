class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans, count, ref = [[]], 0, None
        for x in sorted(nums):
            if x != ref:
                ref = x
                count = len(ans)
            for i in range(len(ans)-count, len(ans)):
                ans.append(ans[i]+[x])
        return ans

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [[1, 2, 2]]
    answers = [[[2],[1],[1,2,2],[2,2],[1,2],[]]]
    test(Solution().subsetsWithDup, arguments, answers, mode='2D')
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)