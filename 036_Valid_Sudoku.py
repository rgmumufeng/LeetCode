class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        seen = sum(([(c, i), (j, c), (i/3, j/3, c)]
                    for i, row in enumerate(board)
                    for j, c in enumerate(row)
                    if c != '.'), [])
        return len(seen) == len(set(seen))

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [[[5, 3, '.'],[6, '.', '.'], ['.', 9, 8]]]
    answers = [True]
    test(Solution().isValidSudoku, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)