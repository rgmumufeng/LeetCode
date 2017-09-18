class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if endWord not in wordList:
            return []
        
        reached, unreached = set([beginWord]), set(wordList)
        if beginWord in unreached:
            unreached.remove(beginWord)
        records = {beginWord: {'parents': set([]), 'kids': set([])}}
        willadd = set([])
        while endWord not in reached:
            for word in reached:
                for i in xrange(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c != word[i]:
                            tmp = word[:i]+c+word[i+1:]
                            if tmp in unreached:
                                willadd.add(tmp)
                                records[word]['kids'].add(tmp)
                                if tmp not in records:
                                    records[tmp] = {'parents': set([word]), 'kids':set([])}
                                else:
                                    records[tmp]['parents'].add(word)
                self.clean(records, word)
                if not records:
                    return []
            unreached.difference_update(willadd)
            reached, willadd = willadd, set([])

        for word in reached:
            if word != endWord:
                self.clean(records, word)
                
        ans = [[beginWord]]
        while True:
            for i in xrange(len(ans)):
                kids = list(records[ans[i][-1]]['kids'])
                if not kids:
                    return ans
                ans[i].append(kids[0])
                for kid in kids[1:]:
                    ans.append(ans[i][:-1]+[kid])
    
    def clean(self, records, word):
        if word in records and not records[word]['kids']:
            parents = records[word]['parents']
            del records[word]
            for p in parents:
                records[p]['kids'].remove(word)
                self.clean(records, p)
                
    

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [("hit", "cog", ["hot","dot","dog","lot","log","cog"]),
                 ("a", "c", ["a", "b", "c"]),
                 ("hot", "dog", ["hot", "dog"]),
                 ("hot", "dog", ["hot","cog","dog","tot","hog","hop","pot","dot"])
                 ]
    answers = [
               [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]],
               [["a", "c"]],
               [],
               [["hot","dot","dog"],["hot","hog","dog"]]
               ]
    test(Solution().findLadders, arguments, answers, inds=None, mode='1D')
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)