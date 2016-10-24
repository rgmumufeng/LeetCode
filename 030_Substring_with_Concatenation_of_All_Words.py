class Solution1(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words:
            return []
        
        length = len(words[0])
        if length == 0:
            return range(len(s)+1)
        
        total_length = length * len(words)
        if total_length > len(s):
            return []
        
        heads = set([word[0] for word in words])
        mp = {}
        for word in words:
            if word not in mp:
                mp[word] = 1
            else:
                mp[word] += 1
        
        res = []
        pi = 0
        while len(s) - pi >= total_length:
            if s[pi] in heads:
                i = pi
                todo = dict(mp)
                while todo and s[i:i+length] in todo:
                    word = s[i:i+length]
                    if todo[word] > 1:
                        todo[word] -= 1
                    else:
                        del todo[word]
                    i += length
                if not todo:
                    res.append(pi)       
            pi += 1
        return res
    
class Solution2(object):
    #Memory Limit Exceeded
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words:
            return []
        
        length = len(words[0])
        if length == 0:
            return range(len(s)+1)
        
        total_length = length * len(words)
        if total_length > len(s):
            return []
        
        from itertools import permutations
        strs = list(set(["".join(x) for x in permutations(words, len(words))]))
        res = []
        pi = 0
        while len(s) - pi >= total_length:
            if s[pi:pi+total_length] in strs:
                res.append(pi)
            pi += 1
        return res


if __name__ == "__main__":
    from leetcodelib import run_testfile
    testfile = __file__.replace('.py', '.yaml')
    
    run_testfile(testfile, Solution1().findSubstring)
    run_testfile(testfile, Solution2().findSubstring, 3)
