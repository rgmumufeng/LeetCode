class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def say(s):
            ref = s[0]
            count = 1
            ans = ""
            for c in s[1:]:
                if c == ref:
                    count += 1
                else:
                    ans += str(count) + ref
                    ref = c
                    count = 1
            return ans + str(count) + ref
        
        ans = '1'
        if n <= 1:
            return ans
        for i in xrange(1, n):
            ans = say(ans)
        return ans

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = range(10)
    answers = ['1', '1', '11', '21', '1211', '111221', '312211', '13112221', '1113213211', '31131211131221']
    test(Solution().countAndSay, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)