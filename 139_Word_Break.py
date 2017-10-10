class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        ref = {}
        for word in wordDict:
            k = word[0]
            if k not in ref:
                ref[k] = []
            ref[k].append(word)
        for k, v in ref.items():
            ref[k] = sorted(v, key=lambda x: len(x), reverse=True)
        
        return self.rec(s, 0, ref)
            
    def rec(self, s, i, ref):
        if i == len(s):
            return True

        if s[i] not in ref:
            return False
        
        for word in ref[s[i]]:
            j = i+len(word)
            print s[i:j], word, s[j:]
            if s[i:j] == word and self.rec(s, j, ref):
                return True
        return False
    
class Solution2(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        status = [True] + [False] * len(s)
        for t in xrange(1, len(s)+1):
            for word in wordDict:
                h = t-len(word)
                if h >= 0 and s[h:t] == word and status[h]:
                    status[t] = True
                    break
        return status[-1]
                    
                

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    #dicts = [["leet", "code"], ["leet", "co"], ["le", "leet", "code"]]
    #arguments = [("leetcode", x) for x in dicts]
    #answers = [True, False, True]
    
    arguments = [("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", 
                  ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])]
    answers = [False]           
    test(Solution2().wordBreak, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)