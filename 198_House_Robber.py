class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        first, second = 0, nums[0]
        for i in xrange(1, len(nums)):
            first, second = second, max(second, first+nums[i])
        return second
    
        
if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [[1, 3, 1]]
    answers = [3]
    test(Solution().rob, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)