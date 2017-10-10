class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x1 = x2 = 0
        for n in nums:
            x2 ^= (x1 & n)
            x1 ^= n
            mask = ~(x1 & x2)
            x1 &= mask
            x2 &= mask
        return x1
        

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [[2, 2, 2, 1]]
    answers = [1]
    test(Solution().singleNumber, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)