class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        nrow = rowIndex+1
        tmp = [[0,0] for _ in xrange(nrow)]
        ans = []
        for i in xrange(nrow):
            tmp[i] = [tmp[i][1], 1]
            for j in xrange(i+1, nrow):
                tmp[j] = [tmp[j][1], tmp[j-1][0]+tmp[j-1][1]]
            ans.append(tmp[-1][1])
        return ans

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [5]
    answers = [[1,5,10,10,5,1]]
    test(Solution().getRow, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)