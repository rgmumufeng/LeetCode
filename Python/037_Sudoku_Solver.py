class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        from itertools import product
        def isvalid(board, row, col, n):
            c = str(n)
            if board[row][col] != '.': return False
            for i in xrange(9):
                if board[row][i] == c: return False
                if board[i][col] == c: return False
                if board[3*int(row/3)+i/3][3*int(col/3)+i%3] == c: return False
            return True
        
        def solve(board):
            for i, j in product(range(9), repeat=2):
                if board[i][j] == ".":
                    for n in xrange(1, 10):
                        if isvalid(board, i, j, n):
                            board[i][j] = str(n)
                            if solve(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False
            return True
        
        solve(board)
        return board

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    
    testfile = __file__.replace('.py', '.yaml')
    run_testfile(testfile, Solution().solveSudoku)