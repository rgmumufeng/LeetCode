class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ans = [0 for _ in xrange(len(num1)+len(num2))]
        for i in xrange(len(num1)):
            for j in xrange(len(num2)):
                c = int(num1[i]) * int(num2[j])
                ans[i+j] += c // 10
                ans[i+j+1] += c % 10

        for i in xrange(len(ans)-1, 0, -1):
            if ans[i] >= 10:
                ans[i-1] += ans[i] // 10
                ans[i] = ans[i] % 10

        for start in xrange(len(ans)):
            if ans[start] != 0:
                break
            
        if start == len(ans):
            return '0'
        return "".join([str(ans[i]) for i in xrange(start, len(ans))]) 
            
        
                    

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [('3', '5'), ('123', '456'), ('5', '33'), ('999', '1')]
    answers = [str(int(x) * int(y)) for (x, y) in arguments]
    test(Solution().multiply, arguments, answers, [1])
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)