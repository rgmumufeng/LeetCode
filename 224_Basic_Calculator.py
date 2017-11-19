class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        tot, opt, stack, i = 0, 1, [], 0
        i = 0
        while i < len(s):
            if s[i].isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                tot += opt * int(s[start:i])
                continue
            if s[i] == '(':
                stack.append((tot, opt))
                tot, opt = 0, 1
            elif s[i] == ')':
                prev_tot, prev_opt = stack.pop()
                tot = prev_tot + prev_opt * tot
                opt = 1
            elif s[i] in '+-':
                opt = (1, -1)[s[i] == '-']
            i += 1
        return tot
    
class Solution2(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        signs = [1, 1]
        tot = i = 0
        while i < len(s):
            if s[i].isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                tot += int(s[start:i]) * signs.pop()
                continue
            elif s[i] in "+-(":
                signs.append(signs[-1]*(1, -1)[s[i]=='-'])
            elif s[i] == ")":
                signs.pop()
            i += 1
        return tot
                
    
    
    

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = ["(1+(4+5+2)-3)+(6+8)", " 21 -   (1 + 2) "]
    answers = [23, 18]
    test(Solution().calculate, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)