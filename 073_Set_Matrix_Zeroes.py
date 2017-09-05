class Solution1(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return matrix
        
        m, n = len(matrix), len(matrix[0])
        
        full_row = []
        col_stat = {k:False for k in xrange(n)}
        for i in xrange(m):
            if all(matrix[i]):
                full_row.append(i)
            else:
                for j in xrange(n):
                    if matrix[i][j] == 0 and not col_stat[j]:
                        col_stat[j] = True
                    else:
                        matrix[i][j] = 0
        zero_col = [j for j, v in col_stat.items() if v]
        if full_row and zero_col:
            for i in full_row:
                for j in zero_col:
                    matrix[i][j] = 0
        return matrix

    
class Solution2(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        
        m, n = len(matrix), len(matrix[0])
        col0 = 1
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    if j == 0:
                        col0 = 0
                    else:
                        matrix[0][j] = 0
                        
        for i in xrange(m-1, -1, -1):
            for j in xrange(n-1, -1, -1):
                col_stat = col0 if j == 0 else matrix[0][j]
                if matrix[i][0] == 0 or col_stat == 0:
                    matrix[i][j] = 0
                    
        return matrix
                        
   

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile, load_testfile
    m1 = [[1, 2, 3], [4, 5, 6]]
    a1 = [[x for x in row] for row in m1]
    
    m2 = [[0, 1, 2], [4, 5, 6]]
    a2 = [[0, 0, 0], [0, 5, 6]]
    
    m3 = [[1, 2, 3], [4, 0, 6]]
    a3 = [[1, 0, 3], [0, 0, 0]]
    
    m4 = [[0, 1, 2], [4, 0, 6]]
    a4 = [[0, 0, 0], [0, 0, 0]]
    
    arguments = [m1, m2, m3, m4]
    answers = [a1, a2, a3, a4]
    #test(Solution()., arguments, answers)
    
    arg_names="matrix"
    testfile = __file__.replace('.py', '.yaml')
    #update_testfile(testfile, arg_names, arguments, answers, 'generate')
    run_testfile(testfile, Solution1().setZeroes)