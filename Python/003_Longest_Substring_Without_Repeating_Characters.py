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
    
class Solution2(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)
        overall, i, ref = 1, 0, {s[0]:0}
        for j in xrange(1, len(s)):
            if s[j] in ref and ref[s[j]] >= i:
                i = ref[s[j]] + 1
            ref[s[j]] = j
            overall = max(overall, j-i+1)
        return overall

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [("abcabcbb",), ("bbbbb",), ("pwwkew",), ("au",), ("dvdf",)]
    answers = [3, 1, 3, 2, 3]
    test(Solution2().lengthOfLongestSubstring, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)