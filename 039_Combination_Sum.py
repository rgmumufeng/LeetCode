class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        ans = [[] for _ in xrange(target+1)]
        for n in xrange(1, target+1):
            if n >= candidates[0]:
                for c in candidates:
                    if c > n:
                        break
                    if c == n:
                        ans[n].append([c])
                    else:
                        for l in ans[n-c]:
                            tmp = sorted(l+[c])
                            if tmp not in ans[n]:
                                ans[n].append(tmp)
        return ans[-1]

    
class Solution2(object):
    def combinationSum(self, candidates, target):
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
                dfs(candidates, target-candidates[i], i, path+[candidates[i]], ans)
        
        candidates.sort()
        ans = []
        dfs(candidates, target, 0, [], ans)
        return ans
        
    
if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [([2, 3, 6, 7], 7)]
    answers = [[[7],[2, 2, 3]]]
    test(Solution2().combinationSum, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)