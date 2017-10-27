class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        keys = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ref = dict(zip(keys, range(1, 27)))
        res = 0
        for c in s:
            res = res * 26 + ref[c]
        return res

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = ['A', 'AA', 'AAA', 'MCB']
    answers = [1, 27, 703, 8868]
    test(Solution().titleToNumber, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)