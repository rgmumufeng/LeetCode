class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, len(nums)-1
        while i <= j:
            if nums[i] > 0:
                i += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
        for k in xrange(i):
            num = abs(nums[k])
            if num <= i:
                nums[num-1] = -abs(nums[num-1])
        for k in xrange(i):
            if nums[k] >= 0:
                return k+1
        return i+1


if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [[-1, 1, 2, 3, 5]]
    answers = [4]
    test(Solution().firstMissingPositive, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)