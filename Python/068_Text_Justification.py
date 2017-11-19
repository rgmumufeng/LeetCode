class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if not words:
            return ["".ljust(maxWidth)]

        ans = []
        h, length = 0, len(words[0])
        for t in xrange(1, len(words)):
            if length + len(words[t]) + 1 <= maxWidth:
                length = length + len(words[t]) + 1
            else:
                s = words[h]
                n = t-h-1
                if n == 0:
                    s = s.ljust(maxWidth)
                else:  
                    extra = maxWidth - length
                    q, r = extra // n, extra % n
                    spaces = ["".ljust(q+2) for _ in xrange(r)] + ["".ljust(q+1) for _ in xrange(n-r)]
                    for i in xrange(len(spaces)):
                        s = s + spaces[i] + words[h+1+i]
                ans.append(s)
                h, length = t, len(words[t])
        ans.append(" ".join(words[h:]).ljust(maxWidth))
        return ans
        

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [(["apple"], 10), (["This", "is", "an", "example", "of", "text", "justification."], 16)]
    answers = [["apple     "], ["This    is    an", "example  of text", "justification.  "]]
    test(Solution().fullJustify, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)