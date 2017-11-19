class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        
        prefix = ''
        i = 0
        while i < len(strs[0]):
            c = strs[0][i]
            for s in strs[1:]:
                if i >= len(s) or s[i] != c:
                    return prefix
            prefix += c
            i += 1
        return prefix


class Solution2(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        i = 0
        while i < len(strs[0]):
            for j in xrange(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return strs[0][:i]
            i += 1
        return strs[0][:i]
            
if __name__ == "__main__":
    from leetcodelib import test
    arguments = [['abc', 'abf', 'ab'], ['abc', 'abf', 'a'], ['abc', 'bcd'], ['abc', 'ae']]
    answers = ['ab', 'a', '', 'a']
    test(Solution2().longestCommonPrefix, arguments, answers)