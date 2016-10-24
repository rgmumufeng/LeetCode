class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mp = [' ', '*', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        ans = ['']
        for d in digits:
            tmp = []
            for s in ans:
                for c in mp[int(d)]:
                    tmp.append(s+c)
            ans = tmp
        return [] if ans == [''] else ans
                

if __name__ == "__main__":
    from leetcodelib import test
    arguments = ['23']
    answers = [['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']]
    test(Solution().letterCombinations, arguments, answers)