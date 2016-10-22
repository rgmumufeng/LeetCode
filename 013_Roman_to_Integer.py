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
    
if __name__ == "__main__":
    from leetcodelib import test
    arguments = ['I', 'III', 'V', 'X', 'XXIII', 'XLVII', 'XCIV', 'MMMCCXCVII']
    answers = [1, 3, 5, 10, 23, 47, 94, 3297]
    test(Solution().romanToInt, arguments, answers)