class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = {}
        for s in strs:
            key = "".join(sorted(s))
            if key not in res:
                res[key] = [s]
            else:
                res[key].append(s)
        return res.values()

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [["eat", "tea", "tan", "ate", "nat", "bat"]]
    answers = [[["ate", "eat","tea"],["nat","tan"],["bat"]]]
    test(Solution().groupAnagrams, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)