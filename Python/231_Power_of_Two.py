# Conventional way of dividing the number by 2
class Solution1(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        n = abs(n)
        while n > 1:
            if n % 2:
                return False
            else:
                n //= 2
        return True
    
# if n is power of 2, its binary form should be "10000...000", then n&(n-1) should be 0
class Solution2(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        return False if n & (n-1) else True
        
if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    #arguments = []
    #answers = []
    #test(Solution()., arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)