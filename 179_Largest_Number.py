class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        l = [str(x) for x in nums]
        l.sort(cmp=lambda s1, s2: cmp(s1+s2, s2+s1), reverse=True)
        return "".join(l).lstrip('0') or '0'

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [[1, 2]]
    answers = ['21']
    test(Solution().largestNumber, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)