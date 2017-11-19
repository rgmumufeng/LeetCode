class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(candidates, target, index, path, ans):
            if target < 0:
                return
            
            if target == 0:
                ans.append(path)
                return
            
            for i in xrange(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                dfs(candidates, target-candidates[i], i+1, path+[candidates[i]], ans)
        
        candidates.sort()
        ans = []
        dfs(candidates, target, 0, [], ans)
        return ans

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [([10, 1, 2, 7, 6, 1, 5], 8)]
    answers = [[[1, 7],[1, 2, 5],[2, 6],[1, 1, 6]]]
    test(Solution().combinationSum2, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)