class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ans = range(len(s))
        for i in xrange(len(s)):
            if s[:i+1] == s[:i+1][::-1]:
                ans[i] = 0
                continue
            else:
                for j in xrange(1, i+1):
                    if s[j:i+1] == s[j:i+1][::-1]:
                        ans[i] = min(ans[i], ans[j-1]+1)
        return ans[-1]
    
    
            
    
if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = ["aab", "aaba"]
    answers = [1, 1]
    test(Solution().minCut, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)