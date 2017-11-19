class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        reached, unreached = set([beginWord]), set(wordList)
        if endWord not in unreached:
            return 0
        count, willadd = 1, set([])
        while endWord not in reached:
            if not unreached:
                return 0
            for word in reached:
                for i in xrange(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        tmp = word[:i] + c + word[i+1:]
                        if tmp in unreached:
                            willadd.add(tmp)
                            unreached.remove(tmp)
            if not willadd:
                return 0
            reached, willadd = willadd, set([])
            count += 1
        return count
    
class Solution2(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        head = set([beginWord])
        tail = set([endWord])
        unreached = set(wordList)
        unreached.remove(endWord)
        count, willadd = 2, set([])
        while True:
            if len(head) > len(tail):
                head, tail = tail, head
            for word in head:
                for i in xrange(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        tmp = word[:i]+c+word[i+1:]
                        if tmp in tail:
                            return count
                        elif tmp in unreached:
                            willadd.add(tmp)
                            unreached.remove(tmp)
            if not willadd:
                return 0
            head, willadd = willadd, set([])
            count += 1
            
            

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    #arguments = [("hit", "cog", ["hot","dot","dog","lot","log","cog"])]
    #answers = [5]
    #test(Solution().ladderLength, arguments, answers)
    
    testfile = __file__.replace('.py', '.yaml')
    #arg_names = "beginWord, endWord, wordList"
    #arguments = []
    #answers = []
    #update_testfile(testfile, arg_names, arguments, answers, mode='add')
    run_testfile(testfile, Solution2().ladderLength, inds=[])