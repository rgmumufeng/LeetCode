class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if not n or not k:
            return ""        
        if n == 1:
            return "1"
        
        nums = range(1, n+1)
        counts = [1]
        for i in xrange(1, n-1):
            counts.append(counts[-1]*nums[i])
        if k > counts[-1]*n:
            return ""
                
        s, k = "", k-1
        for i in counts[::-1]:
            q, k = k // i, k % i
            s += str(nums[q])
            nums = nums[:q] + nums[q+1:]
        return s + str(nums[0])
        

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [(4, 11), (1, 1)]
    answers = ["2413", "1"]
    test(Solution().getPermutation, arguments, answers, [1])
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)