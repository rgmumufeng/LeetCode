class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        tot, num, opt, prev = 0, None, "+", []
        i = 0
        while i <= len(s):
            if i < len(s) and s[i].isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                num = int(s[start:i])
                continue
            c = s[i] if i < len(s) else "+"
            if c in "+-":
                tot = self.runmath(tot, num, opt)
                if opt in "*/":
                    tot = self.runmath(prev[0], tot, prev[1])
                    prev = []
                opt, num = c, None
            elif c in "*/":
                if opt in "+-":
                    prev = [tot, opt]
                    tot = num
                else:
                    tot = self.runmath(tot, num, opt)
                opt, num = c, None
            i += 1
        return tot 

    def runmath(self, a, b, opt):
        if opt == '+':
            return a+b
        if opt == '-':
            return a-b
        if opt == '*':
            return a*b
        if opt == '/':
            return a/b
        
                    

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [" 1 +  2+3*4 /5 +6/7  "]
    answers = [eval(s) for s in arguments]
    test(Solution().calculate, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)