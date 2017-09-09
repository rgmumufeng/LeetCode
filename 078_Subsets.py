class Solution1(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        
        n = nums.pop()
        ans = []
        for x in self.subsets(nums):
            ans.append(x)
            ans.append(x+[n])
        return ans

    
class Solution2(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        for n in nums:
            for i in xrange(len(ans)):
                ans.append(ans[i]+[n])
        return ans
        
        

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [[1, 2, 3]]
    answers = [[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]]
    test(Solution2().subsets, arguments, answers, mode='2D_sets')
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)