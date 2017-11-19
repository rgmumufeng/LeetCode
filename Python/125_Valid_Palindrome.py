class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 1:
            return True
        
        i, j = 0, len(s)-1
        while i < j:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            if s[i].lower() == s[j].lower():
                i, j = i+1, j-1
            else:
                return False
        return True

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = ["A man, a plan, a canal: Panama", "race a car"]
    answers = [True, False]
    test(Solution().isPalindrome, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)