class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n >= 5:
            n = n/5
            res += n
        return res

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [1000, 4617]
    answers = [249, 1151]
    test(Solution().trailingZeroes, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)