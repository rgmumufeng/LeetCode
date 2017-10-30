class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board or not board[0]:
            return []
        ref = {}
        
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] not in ref:
                    ref[board[i][j]] = []
                ref[board[i][j]].append((i, j))
        res = set([])
        for word in words:
            if not word:
                res.add(word)
            elif word not in res and word[0] in ref:
                for ind in ref[word[0]]:
                    if self._search(board, ind, word, 0):
                        res.add(word)
                        break
        return list(res)

    def _search(self, board, (i0, j0), word, h):
        if h == len(word):
            return True
        if i0 < 0 or i0 >= len(board) or j0 < 0 or j0 >= len(board[0]) or board[i0][j0] != word[h]:
            return False
        board[i0][j0] = "#"
        for ind in zip([i0+1, i0-1, i0, i0], [j0, j0, j0+1, j0-1]):
            res = self._search(board, ind, word, h+1)
            if res:
                break
        board[i0][j0] = word[h]
        return res

    
class Solution2(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        root = {}
        for word in words:
            node = root
            for c in word:
                node = node.setdefault(c, {})
            node[""] = word
           
        res = []
        for i in xrange(len(board)):
            for j in xrange(len(board[i])):
                self.search(board, i, j, root, res)
        return res
        
    def search(self, board, i, j, node, res):
        if "" in node and node[""] != None:
            res.append(node[""])
            node[""] = None
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]) or board[i][j] not in node:
            return
        node = node[board[i][j]]
        c, board[i][j] = board[i][j], '#'
        for (ii, jj) in zip([i+1, i-1, i, i], [j, j, j+1, j-1]):
            self.search(board, ii, jj, node, res)
        board[i][j] = c
        
        
        
        
if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    board = [['o','a','a','n'],['e','t','a','e'],['i','h','k','r'],['i','f','l','v']]
    words = ["oath","pea","eat","rain"]
    arguments = [(board, words)]
    answers = [["eat","oath"]]
    test(Solution2().findWords, arguments, answers, mode='1D')
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)