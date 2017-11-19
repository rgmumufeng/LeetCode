class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mp = {')': '(', ']': '[', '}': '{'}
        stack = []
        for c in s:
            if c in mp.values():
                stack.append(c)
            elif not stack or mp[c] != stack.pop():
                return False
        return False if stack else True
                

if __name__ == "__main__":
    from leetcodelib import test
    arguments = ['()', '))()', '(())', '[){}', '{(})', '{[]}', '()(']
    answers = [True, False, True, False, False, True, False]
    test(Solution().isValid, arguments, answers)