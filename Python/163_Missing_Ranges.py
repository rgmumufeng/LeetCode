class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        
        if not nums:
            return [self.update(lower, upper)]
        
        res = []
        if nums[0] != lower:
            res.append(self.update(lower, nums[0]-1))
        for i in xrange(1, len(nums)):
            if nums[i] - nums[i-1] > 1:
                res.append(self.update(nums[i-1]+1, nums[i]-1))
        if nums[-1] != upper:
            res.append(self.update(nums[-1]+1, upper))
        return res
                
    def update(self, h, t):
        return str(h) if h == t else "{}->{}".format(h, t) 
            
            
if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    #arguments = []
    #answers = []
    #test(Solution()., arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)