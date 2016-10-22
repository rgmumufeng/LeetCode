class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MAX = 2147483647
        rlim = INT_MAX / 10
            
        x, sign = (x, 1) if x >= 0 else (-x, -1)
        r = 0
        while x > 0 and r < rlim:
            r = r * 10 + x % 10
            x = x // 10
        
        if x <= 0:
            return r * sign
        
        if r == rlim and x <= 7:
            return (r*10+x) * sign
        else:
            return 0

if __name__ == "__main__":
    from leetcodelib import test
    arguments = [0, 123, -2147483647, -80000, 1463847422, -2147483412]
    answers = [0, 321, 0, -8, 0, -2143847412]
    test(Solution().reverse, arguments, answers)

