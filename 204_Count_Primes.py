class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        status = [True] * n
        count = 0
        for i in xrange(2, n):
            if status[i]:
                count += 1
                tmp = i << 1
                while tmp < n:
                    status[tmp] = False
                    tmp += i
        return count
                    
if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [16, 499979]
    answers = [6, 41537]
    test(Solution().countPrimes, arguments, answers, inds=[])
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)