class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) <= 2 or len(board[0]) <= 2:
            return 
        
        m, n = len(board), len(board[0])
        for i in xrange(m):
            self.rec(i, 0, board)
            self.rec(i, n-1, board)
        for j in xrange(n):
            self.rec(0, j, board)
            self.rec(m-1, j, board)
        
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"
        return ["".join(x) for x in board]
        
    
    def rec(self, i, j, board):
        if board[i][j] != 'O':
            return
        board[i][j] = '#'
        for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= x < len(board) and 0 <= y < len(board[0]):
                self.rec(x, y, board)
                

class Solution2(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) <= 2 or len(board[0]) <= 2:
            return 
        m, n = len(board), len(board[0])
        stack = [(i, j) for k in xrange(m+n) for (i, j) in [(0, k), (m-1, k), (k, 0), (k, n-1)]]
        while stack:
            i, j = stack.pop()
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = '#'
                stack += [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
                
        for i in xrange(m):
            for j in xrange(n):
                board[i][j] = 'XO'[board[i][j] == '#']
        return ["".join(x) for x in board]

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    boards = [["XXXX", "XOOX", "XXOX", "XOXX"],
              ["XOXX","OXOX","XOXO","OXOX","XOXO","OXOX"],
              ["OOO","OOO","OOO"],
              ["OXOOOX","OOXXXO","XXXXXO","OOOOXX","XXOOXO","OOXXXX"]]
    arguments = [[list(x) for x in board] for board in boards]
    answers = [["XXXX", "XXXX", "XXXX", "XOXX"],
               ["XOXX","OXXX","XXXO","OXXX","XXXO","OXOX"],
               ["OOO","OOO","OOO"],
               ["OXOOOX","OOXXXO","XXXXXO","OOOOXX","XXOOXO","OOXXXX"]]
    test(Solution2().solve, arguments, answers, inds=None)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)