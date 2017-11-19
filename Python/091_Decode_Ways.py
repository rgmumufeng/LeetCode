class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0
        
        ans = [1, 1]
        for i in xrange(1, len(s)):
            if not ans[-1] and not ans[-2]:
                return 0
            ans1 = ans[-1] if s[i] in '123456789' else 0
            ans2 = ans[-2] if 10 <= int(s[i-1:i+1]) <= 26 else 0
            ans.append(ans1+ans2)
        return ans[-1]
                

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = ["12", "103", "1030"]
    answers = [2, 1, 0]
    test(Solution().numDecodings, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)