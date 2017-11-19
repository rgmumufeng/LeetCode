# Solution 1 brutal force
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        ref = [[int(matrix[i][j]) for j in xrange(n)] for i in xrange(m)]
        maxl = max(ref[m-1]+[ref[i][n-1] for i in xrange(m)])
        for i in xrange(m-2, -1, -1):
            for j in xrange(n-2, -1, -1):
                if matrix[i][j] == '0':
                    ref[i][j] = 0
                else:
                    ref[i][j] = min(ref[i+1][j], ref[i][j+1], ref[i+1][j+1])+1
                maxl = max(ref[i][j], maxl)
        return maxl ** 2

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    matrix1 = [list("000") for _ in xrange(4)]
    matrix2 = [["1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","0"],["1","1","1","1","1","1","1","0"],["1","1","1","1","1","0","0","0"],["0","1","1","1","1","0","0","0"]]
    arguments = [matrix1, matrix2]
    answers = [0, 16]
    test(Solution().maximalSquare, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)