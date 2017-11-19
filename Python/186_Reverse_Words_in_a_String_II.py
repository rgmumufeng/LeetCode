class Solution(object):
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        self.reverse(str, 0, len(str)-1)
        h = 0
        for t in xrange(len(str)):
            if str[t] == ' ':
                self.reverse(str, h, t-1)
                h = t+1
            elif t == len(str)-1:
                self.reverse(str, h, t)
                
        
    def reverse(self, str, i, j):
        while i < j:
            str[i], str[j] = str[j], str[i]
            i += 1
            j -= 1
        

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arg = 'the sky is blue'
    ans = 'blue is sky the'
    arguments = [list(arg)]
    answers = [list(ans)]
    test(Solution().reverseWords, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)