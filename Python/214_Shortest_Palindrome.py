class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        maxj, c = 1, 0
        while c <= len(s)/2:
            i = j = c
            while j+1 < len(s) and s[j+1] == s[j]:
                j += 1
            if i > len(s)-j-1:
                break
            c = j+1
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            if i < 0:
                maxj = max(maxj, j)
        return s[maxj:][::-1]+s
            

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = ["aacecaaa", "abcd", "ba"]
    answers = ["aaacecaaa", "dcbabcd", "aba"]
    test(Solution().shortestPalindrome, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)