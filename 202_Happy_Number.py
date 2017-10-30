class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sqsum, reached = n, set([])
        while sqsum != 1:
            reached.add(sqsum)
            i, sqsum = sqsum, 0
            while i > 0:
                sqsum += (i % 10) ** 2
                i /= 10
            if sqsum in reached:
                return False
        return True


if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [7]
    answers = [True]
    test(Solution().isHappy, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)