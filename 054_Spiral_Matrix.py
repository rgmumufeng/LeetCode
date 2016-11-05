class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        ans = []
        m, n = len(matrix), len(matrix[0])
        if m < n:
            maxk, check, isrow = m/2, m%2, False
        else:
            maxk, check, isrow = n/2, n%2, True
        
        for k in xrange(maxk):
            for j in xrange(k, n-k-1):
                ans.append(matrix[k][j])
            for i in xrange(k, m-k-1):
                ans.append(matrix[i][n-k-1])
            for j in xrange(n-k-1, k, -1):
                ans.append(matrix[m-k-1][j])
            for i in xrange(m-k-1, k, -1):
                ans.append(matrix[i][k])
        
        if check:
            if isrow:
                for i in xrange(maxk, m-maxk):
                    ans.append(matrix[i][maxk])
            else:
                for j in xrange(maxk, n-maxk):
                    ans.append(matrix[maxk][j])
        return ans
                     
                     
class Solution2(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        
        ans = []
        k, m, n = 0, len(matrix), len(matrix[0])
        while True:
            if k == m or k == n:
                return ans
            if k == m-1:
                return ans + [matrix[k][j] for j in xrange(k, n)]
            if k == n-1:
                return ans + [matrix[i][k] for i in xrange(k, m)]
            
            for j in xrange(k, n-1):
                ans.append(matrix[k][j])
            for i in xrange(k, m-1):
                ans.append(matrix[i][n-1])
            for j in xrange(n-1, k, -1):
                ans.append(matrix[m-1][j])
            for i in xrange(m-1, k, -1):
                ans.append(matrix[i][k])    
            k, m, n = k+1, m-1, n-1

            
         
        
   

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    
    import numpy as np
    shape = (2, 1)
    m1 = np.arange(1, shape[0]*shape[1]+1).reshape(shape).tolist()
    for i in xrange(shape[0]):
        print m1[i]
    print
    print Solution2().spiralOrder(m1)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)