class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return -1
        
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        i = 0
        d, r = abs(dividend), abs(divisor)
        while d >= r:
            d -= r
            i += 1
        
        return -i if max(dividend, divisor) > 0 and min(dividend, divisor) < 0 else i
    

class Solution2(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return -1
        
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        
        def helper(d, s):
            if d < s:
                return 0, d
            
            k = d & 0x1
            d >>= 1
            m, r = helper(d, s)
            m += m
            r += r+k
            if r >= s:
                m += 1
                r -= s
            return m, r
        
        i = helper(abs(dividend), abs(divisor))[0]
        return -i if max(dividend, divisor) > 0 and min(dividend, divisor) < 0 else i


# Solution3 is a copy of 's solution from
# https://discuss.leetcode.com/category/37/divide-two-integers
class Solution3(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)
    
if __name__ == "__main__":
    from leetcodelib import test
    from random import randint
    INT_MIN, INT_MAX = -2147483648, 2147483647
    arguments = [(INT_MIN, -1)] + [(randint(INT_MIN, INT_MAX), randint(INT_MIN, INT_MAX)) for _ in xrange(100)]
    answers = [INT_MAX] + [int(float(x[0])/float(x[1])) for x in arguments[1:]]
    test(Solution2().divide, arguments, answers)
    test(Solution3().divide, arguments, answers)