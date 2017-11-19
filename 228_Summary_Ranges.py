class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        for i in xrange(len(nums)):
            if i == 0:
                start = nums[0]
            n = nums[i+1] if i < len(nums)-1 else nums[-1]+2 
            if n - nums[i] > 1:
                if nums[i] == start:
                    res.append(str(start))
                else:
                    res.append("{}->{}".format(start, nums[i]))
                start = n
        return res
        
                           

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    #arguments = []
    #answers = []
    #test(Solution()., arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)