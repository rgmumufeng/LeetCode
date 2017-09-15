class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        ans = [[1]]
        for i in xrange(numRows-1):
            tmp = [1]
            for j in xrange(len(ans[-1])-1):
                tmp.append(ans[-1][j]+ans[-1][j+1])
            tmp.append(1)
            ans.append(tmp)
        return ans

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [6]
    answers = [[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1],
 [1,5,10,10,5,1]
]]
    test(Solution().generate, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)