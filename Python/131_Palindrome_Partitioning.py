class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ans = [[[]]]
        for i in xrange(0, len(s)):
            ans.append([x+[s[i]] for x in ans[-1]])
            for head in self.find(i, s):
                ans[-1].extend([x+[s[head:i+1]] for x in ans[head]])
        return ans[-1]
        
    def find(self, tail, s):
        ans = []
        for head in xrange(tail):
            if s[head:tail+1] == s[head:tail+1][::-1]:
                ans.append(head)
        return ans
            

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = ["aab", "aaba"]
    answers = [[["a", "a", "b"], ["aa", "b"]],
               [["a", "a", "b", "a"], ["aa", "b", "a"], ["a", "aba"]]]
    test(Solution().partition, arguments, answers, mode='1D')
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)