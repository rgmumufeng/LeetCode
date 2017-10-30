class WordDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node[""] = {}
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self._search(word, 0, self.ref)
        
    def _search(self, word, h, node):
        if h == len(word):
            return True if "" in node else False
        
        if word[h] != '.':
            return False if word[h] not in node else self._search(word, h+1, node[word[h]])
        else:
            for c in node:
                if self._search(word, h+1, node[c]):
                    return True
            return False

                 
if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    #arguments = []
    #answers = []
    #test(Solution()., arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)