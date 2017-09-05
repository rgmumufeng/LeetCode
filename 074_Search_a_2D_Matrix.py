class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        
        n, m = len(matrix), len(matrix[0])
        i, j = 0, m*n
        while j - i > 1:
            mid = (i+j)/2
            if target < matrix[mid//m][mid%m]:
                j = mid
            else:
                i = mid
        return target == matrix[i//m][i%m]
            

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    m1 = [[0, 1, 2],[4, 5, 6]]
    t = [-1, 0, 1, 3, 6, 7]
    arguments = [(m1, x) for x in t]
    answers = [False, True, True, False, True, False]
    test(Solution().searchMatrix, arguments, answers, inds=None)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)