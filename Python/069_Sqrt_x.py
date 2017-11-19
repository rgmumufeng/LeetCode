class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        elif x < 4:
            return 1
            
        i = 2
        while i**2 <= x:
            if (i+1)**2 > x:
                return i
            else:
                delta = self.mySqrt(x/(i**2))
                if delta == 1:
                    i += delta
                else:
                    i *= delta
            
            

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    import math
    arguments = [0, 2, 4, 9, 24, 79]
    answers = [int(math.sqrt(x)) for x in arguments]
    test(Solution().mySqrt, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)