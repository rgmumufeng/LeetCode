class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        board = [list(x) for x in board]

        if word and (not board or not board[0]):
            return False

        def walk(i, j, ind):
            if ind == len(word):
                return True
            
            if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j] != word[ind]:
                return False
            
            tmp, board[i][j] = board[i][j], "#"
            status = walk(i-1, j, ind+1) or walk(i+1, j, ind+1) or walk(i, j-1, ind+1) or walk(i, j+1, ind+1)
            board[i][j] = tmp
            return status

        for i in xrange(len(board)):   
            for j in xrange(len(board[0])):
                if walk(i, j, 0):
                    return True
        return False
                         
           

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    b1 = ["ABCE", "SFCS", "ADEE"]
    b2 = ["aa"]
    b3 = ["ABCE","SFES","ADEE"]
    b4 = ["aaa","abb","abb","bbb","bbb","aaa","bbb","abb","aab","aba"]

     
    arguments = [(b1, "ABCCED"), (b1, "SEE"), (b1, "ABCB"), (b2, "aaa"), (b3, "ABCESEEEFS"), (b4, "aabaaaabbb")]
    answers = [True, True, False, False, True, False]
    test(Solution().exist, arguments, answers, inds=1)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)