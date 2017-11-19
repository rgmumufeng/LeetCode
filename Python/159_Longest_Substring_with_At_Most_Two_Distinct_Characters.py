class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 2:
            return len(s)
        
        h, t = [], []
        recent, overall = 0, 0
        for i in xrange(len(s)):
            if len(h) == 0 or (len(h) == 1 and s[i] != s[h[0]]):
                h.append(i)
                t.append(i)
            elif s[i] == s[h[0]]:
                t[0] = i
            elif s[i] == s[h[1]]:
                t[1] = i
            else:
                h = [min(t)+1, i]
                t = [max(t), i]
            recent = t[0] - h[0] + 1 if len(h) == 1 else max(t) - min(h) + 1
            overall = max(recent, overall)
            #print h, t, recent, overall
        return overall

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = ["eceba", "aba"]
    answers = [3, 3]
    test(Solution().lengthOfLongestSubstringTwoDistinct, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)