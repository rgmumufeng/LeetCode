class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ref, used = {}, set()
        for i in xrange(len(s)):
            if s[i] not in ref:
                if t[i] in used:
                    return False
                ref[s[i]] = t[i]
                used.add(t[i])
            elif ref[s[i]] != t[i]:
                return False
        return True

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [('egg', 'add'), ('ab', 'aa')]
    answers = [True, False]
    test(Solution().isIsomorphic, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)