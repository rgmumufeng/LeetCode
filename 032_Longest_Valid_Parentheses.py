class Solution1(object):
    #Time Limit Exceeded
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return 0
        
        mp = {"(": 1, ")": -1}
        maxlen = 0
        i = 0
        for i in xrange(len(s)):
            if len(s)-i <= maxlen:
                break
            if s[i] == ")":
                continue

            counter = [1]
            j = i + 1
            while j < len(s):
                c = counter[-1] + mp[s[j]]
                if c == 0:
                    maxlen = max(maxlen, j-i+1)
                if c >= 0:
                    counter.append(c)
                    j += 1
                else:
                    break
        return maxlen
    
class Solution2(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return 0
                
        maxlen = 0
        heads = [None]
        for i in xrange(1, len(s)):
            if s[i] == '(':
                head = None
            else:
                j = i-1 if not heads[i-1] else heads[i-1]-1
                if s[j] == ')':
                    head = None
                elif j == 0 or heads[j-1] == None:
                    head = j
                else:
                    head = heads[j-1]
            if head != None:
                maxlen = max(maxlen, i-head+1)
            heads.append(head)
        return maxlen
                
       
if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile    
    arguments = ["()()"]
    answers = [4]
    test(Solution2().longestValidParentheses, arguments, answers)
    
    testfile = __file__.replace('.py', '.yaml')  
    run_testfile(testfile, Solution2().longestValidParentheses)