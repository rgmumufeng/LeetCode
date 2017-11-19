class Solution1(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        m, n = x, 0
        while m > 0:
            m = m // 10
            n += 1
         
        while n > 1:
            q, r = x // 10, x % 10
            x = (x//10) - (x%10)*10**(n-2)
            if x == 0:
                return True
            if x < 0:         
                return False
            if x >= 10 ** (n-2):
                return False
            n -= 2
        return True


class Solution2(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0:
            return True
            
        if x < 0 or x % 10 == 0:
            return False
            
        half = 0
        while x > half:
            x, v = divmod(x, 10)
            half = half * 10 + v
            
        if half == x or half / 10 == x:
            return True
        else:
            return False
        
class Solution3(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x and x%10 == 0):
            return False
        
        res = 0
        while x > res:
            res = res * 10 + x % 10
            x /= 10
        return x == res or x == res/10


if __name__ == "__main__":
    from leetcodelib import test
    arguments = [(1,), (11,), (12,), (32123,), (43211234,), (-12321,), (12515,)]
    answers = [True, True, False, True, True, False, False]
    test(Solution1().isPalindrome, arguments, answers)
    test(Solution2().isPalindrome, arguments, answers)
    test(Solution3().isPalindrome, arguments, answers)

