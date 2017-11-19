class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens:
            return 0
        
        def add(b, a):
            return a + b
        def sub(b, a):
            return a - b
        def pro(b, a):
            return a * b
        def div(b, a):
            return a / b
        
        ref = {"+": add, "-": sub, "*": pro, "/": div}
        stack = []
        for x in tokens:
            if x not in ref:
                stack.append(float(x))
            else:
                tmp = ref[x](stack.pop(), stack.pop())
                stack.append(int(tmp))
        return int(stack.pop())
                        

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [["2", "1", "+", "3", "*"], ["4", "13", "5", "/", "+"], ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]]
    answers = [9, 6, 22]
    test(Solution().evalRPN, arguments, answers, inds=[2])
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)