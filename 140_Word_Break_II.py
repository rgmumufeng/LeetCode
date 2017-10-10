class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        status = [[] for _ in xrange(len(s)+1)]
        status[0].append([])
        for t in xrange(1, len(s)+1):
            for i in xrange(len(wordDict)):
                h = t - len(wordDict[i])
                if h >= 0 and s[h:t] == wordDict[i] and status[h]:
                    status[t].append(i)
        if not status[-1]:
            return []
        
        return self.translate(len(status)-1, status, wordDict)
    
    def translate(self, i, status, wordDict):
        if status[i] and isinstance(status[i][0], int):
            tmp = []
            for x in status[i]:
                word = wordDict[x]
                j = i - len(word)
                if j != 0:
                    tmp.extend([s+" "+word for s in self.translate(j, status, wordDict)])
                else:
                    tmp.append(word)
            status[i] = tmp
        return status[i]

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [("catsanddog", ["cat", "cats", "and", "sand", "dog"])]
    answers = [["cats and dog", "cat sand dog"]]
    
    #arguments = [("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    #              ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])]
    #answers = ['a']
    
    
    test(Solution().wordBreak, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)