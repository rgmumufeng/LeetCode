class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        
        ref, count, tail = None, 0, 0
        for i in xrange(len(nums)):
            if nums[i] != ref or count < 2:
                nums[tail] = nums[i]
                tail += 1
                if nums[i] != ref:
                    count = 1
                    ref = nums[i]
                else:
                    count += 1
        return tail
                

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [[1, 1, 1, 2, 2, 2, 3]]
    answers = [5]
    test(Solution().removeDuplicates, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)