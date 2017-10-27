class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if x == 0 or x == 1:
            return x
        
        if n > 0:
            m, c = n, 1
        else:
            m, c = -n, 0
        
        l = []
        while m > 1:
            l.append(m % 2)
            m /= 2
        res = x
        for i in l[::-1]:
            res *= res
            if i == 1:
                res *= x
        return res if c else 1./res

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [(3, 9), (2, 7), (4, 1), (0, 0), (9, 0), (1, 20), (9, -252)]
    answers = [x**n for (x, n) in arguments]
    test(Solution().myPow, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)