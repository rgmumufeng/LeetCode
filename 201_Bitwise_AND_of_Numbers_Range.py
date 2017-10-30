class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        c = n-m+1
        count = 0
        while c > 2**count:
            count += 1
        for _ in xrange(count):
            m >>= 1
            n >>= 1
        res = m & n
        for _ in xrange(count):
            res <<= 1
        return res
    
class Solution2(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = m
        for i in xrange(m+1, n+1):
            res &= i
        return res
    
class Solution3(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        count = 1
        while m != n:
            count <<= 1
            m >>= 1
            n >>= 1
        return m * count
        
            

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [(5, 7), (19, 40), (32516, 261701)]
    answers = [Solution2().rangeBitwiseAnd(m, n) for m, n in arguments]
    test(Solution().rangeBitwiseAnd, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)