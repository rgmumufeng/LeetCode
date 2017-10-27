class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        x, res = n, 0
        for _ in xrange(32):
            res <<= 1
            res += x & 1
            x >>= 1
        return res

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [43261596]
    answers = [964176192]
    test(Solution().reverseBits, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)