class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if not haystack or len(needle) > len(haystack):
            return -1
        
        pi = 0
        while len(haystack)-pi >= len(needle):
            if haystack[pi] == needle[0]:
                i, j = pi, 0
                while haystack[i] == needle[j]:
                    i += 1
                    j += 1
                    if j == len(needle):
                        return pi
            pi += 1
        return -1
                
if __name__ == "__main__":
    from leetcodelib import test
    arguments = [('ab', 'a'), ('baab', 'aa'), ('baab', 'abc')]
    answers = [0, 1, -1]
    test(Solution().strStr, arguments, answers)