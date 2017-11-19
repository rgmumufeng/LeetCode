class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node[""] = {}
            
    def _search(self, word):
        node = self.root
        for c in word:
            if c not in node:
                return {}
            node = node[c]
        return node
                
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        return True if "" in self._search(word) else False
            
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return True if self._search(prefix) else False
        

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    obj = Trie()
    word = prefix = 'a'
    obj.insert(word)
    param_2 = obj.search(word)
    param_3 = obj.startsWith(prefix)
    print param_2, param_3, obj.ref
    
    #arguments = []
    #answers = []
    #test(Solution()., arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)