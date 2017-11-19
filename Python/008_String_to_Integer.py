class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        rmax = INT_MAX / 10
        
        mp = dict([('%d'%i, i) for i in xrange(10)])
        signs = {'+': 1, '-': -1}
        
        h = 0
        while h < len(str) and str[h] == ' ':
            h += 1
        if h == len(str):
            return 0
        
        if str[h] in signs:
            sign = signs[str[h]]
            h += 1
        else:
            sign = 1
            
        r = 0
        while h < len(str) and str[h] in mp:
            digit = mp[str[h]]
            if r < rmax or (r == rmax and (digit <= 7 or (digit == 8 and sign == -1))):
                r = r * 10 + digit
                h += 1
            else:
                return INT_MAX if sign == 1 else INT_MIN

        return sign * r

class Solution2(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX  = 2147483647
        INT_MIN  = -2147483648
        rmax = 214748364
        ref = dict([("{}".format(i), i) for i in xrange(10)])
        signs = {"+":1, "-":-1}
        
        res, sign, i = 0, 1, 0
        while i < len(str) and str[i] == ' ':
            i += 1
        if i < len(str) and str[i] in signs:
            sign = signs[str[i]]
            i += 1
        while i < len(str) and str[i] in ref:
            digit = ref[str[i]]
            if res < rmax or (res == rmax and (digit < 8 or (digit == 8 and sign < 0))):
                res = res * 10 + digit
                i += 1
            else:
                return INT_MAX if sign > 0 else INT_MIN
        return res * sign
                
        
        

if __name__ == "__main__":
    from leetcodelib import test
    arguments = [("2147483647",), ("-3f3",), ("+314",), ("+0000",), ("-2147483649",), ("2247483647",), ("f3",)]
    answers = [2147483647, -3, 314, 0, -2147483648, 2147483647, 0]
    test(Solution2().myAtoi, arguments, answers)
    