class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ref = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        s = ''
        while True:
            n -= 1
            s = ref[n%26]+s
            n = n/26
            if n == 0:
                return s

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    #arguments = []
    #answers = []
    #test(Solution()., arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)