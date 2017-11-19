class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if not n:
            return []
        
        matrix = [[None for j in xrange(n)] for i in xrange(n)]
        
        c = 1
        for k in xrange(n/2):
            for j in xrange(k, n-k-1):
                matrix[k][j] = c
                c += 1
            for i in xrange(k, n-k-1):
                matrix[i][n-k-1] = c
                c += 1
            for j in xrange(n-k-1, k, -1):
                matrix[n-k-1][j] = c
                c += 1
            for i in xrange(n-k-1, k, -1):
                matrix[i][k] = c
                c += 1
                
        if n % 2:
            matrix[n/2][n/2] = c
        
        return matrix


if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    n = 5
    m = Solution().generateMatrix(n)
    for row in m:
        print row
    print
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)