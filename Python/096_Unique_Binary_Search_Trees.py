class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        
        ans = [1, 1]
        for i in xrange(2 , n+1):
            tmp = 2*(sum([ans[j]*ans[i-j-1] for j in xrange(i/2)]))
            if i % 2 == 1:
                tmp += ans[i/2] ** 2
            ans.append(tmp)
        return ans[-1]
    
if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [3, 4, 5, 6]
    answers = [5, 14, 42, 132]
    test(Solution().numTrees, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)