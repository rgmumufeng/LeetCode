class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        x, res =n, 0
        while x > 0:
            res += x & 1
            x >>= 1
        return res
        

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [1]
    answers = [1]
    test(Solution().hammingWeight, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)