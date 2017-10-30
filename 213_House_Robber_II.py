class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        
        pre1, yes1 = nums[0], max(nums[:2])
        pre2, yes2 = 0, nums[1]
        for i in xrange(2, len(nums)-1):
            pre1, yes1 = yes1, max(yes1, pre1+nums[i])
            pre2, yes2 = yes2, max(yes2, pre2+nums[i])
        return max(yes1, pre2+nums[len(nums)-1])
            

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    #arguments = []
    #answers = []
    #test(Solution()., arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)