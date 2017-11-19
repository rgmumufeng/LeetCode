class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        keys = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        values = [1, 5, 10, 50, 100, 500, 1000]
        mp = dict(zip(keys, values))
        i = 0
        num = 0
        while i < len(s):
            n1 = mp[s[i]]
            n2 = mp[s[i+1]] if i < len(s)-1 else -1
            if n1 < n2:
                num -= n1
            else:
                num += n1
            i += 1
        return num
    
class Solution2(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        keys = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        values = [1, 5, 10, 50, 100, 500, 1000]
        ref = dict(zip(keys, values))
        res = 0
        for i in xrange(len(s)-1):
            res = res-ref[s[i]] if ref[s[i+1]] > ref[s[i]] else res+ref[s[i]]
        return res + ref[s[-1]]
if __name__ == "__main__":
    from leetcodelib import test
    arguments = ['I', 'III', 'V', 'X', 'XXIII', 'XLVII', 'XCIV', 'MMMCCXCVII']
    answers = [1, 3, 5, 10, 23, 47, 94, 3297]
    test(Solution2().romanToInt, arguments, answers)