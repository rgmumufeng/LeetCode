class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = list(s)
        i = h = 0
        while h < len(l):
            while h < len(l) and l[h] == ' ':
                h += 1
            if h == len(l):
                break
            if i != 0:
                l[i] = ' '
                i += 1
            t = h
            while t < len(l) and l[t] != ' ':
                l[i] = l[t]
                i += 1
                t += 1
            h = t
        self.reverse(0, i-1, l)
        
        h = 0
        while h < i:
            t = h
            while t < i and l[t] != ' ':
                t += 1
            self.reverse(h, t-1, l)
            h = t+1
            
        return "".join(l[0:i])
        
    def reverse(self, i, j, l):
        while i < j:
            l[i], l[j] = l[j], l[i]
            i += 1
            j -= 1
        return
        

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = ["   the   sky  is   blue     "]
    answers = [" ".join(s.split()[::-1]) for s in arguments]
    test(Solution().reverseWords, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)