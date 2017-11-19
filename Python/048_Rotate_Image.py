class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        for i in xrange(n-1):
            for j in xrange(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        for i in xrange(n):
            for j in xrange(n/2):
                matrix[i][j], matrix[i][~j] = matrix[i][~j], matrix[i][j]
                
        return matrix
    
class Solution2(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        matrix = matrix[::-1]
        
        for i in xrange(n-1):
            for j in xrange(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

                
        return matrix

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [[[1, 2], [3, 4]]]
    answers = [[[3, 1], [4, 2]]]
    test(Solution2().rotate, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)