class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        if n == 0:
            return 0
        minsum = [0 for _ in xrange(n+1)]
        for i in xrange(n-1, -1, -1):
            tmp = triangle[i]
            for j in xrange(i+1):
                tmp[j] += min(minsum[j], minsum[j+1])
            minsum = tmp
        return minsum[0]

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]]
    answers = [11]
    test(Solution().minimumTotal, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)