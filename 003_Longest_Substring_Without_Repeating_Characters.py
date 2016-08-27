class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, maxlen = 0, 0
        appeared = {}
        for j in xrange(len(s)):
            if s[j] in appeared and appeared[s[j]] >= i:
                maxlen = max(j-i, maxlen)
                i = appeared[s[j]] + 1
                if len(s) - i <= maxlen:
                    return maxlen
            appeared[s[j]] = j
        return max(maxlen, len(s)-i)

if __name__ == "__main__":
    from leetcodelib import test
    arguments = [("abcabcbb",), ("bbbbb",), ("pwwkew",), ("au",), ("dvdf",)]
    answers = [3, 1, 3, 2, 3]
    test(Solution().lengthOfLongestSubstring, arguments, answers)

