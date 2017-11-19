class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        return self.search(0, len(nums), nums)
        
    def search(self, i, j, nums):
        if i == j-1 or nums[i] < nums[j-1]:
            return nums[i]
        mid = (i+j)/2
        return min(self.search(i, mid, nums), self.search(mid, j, nums))
        
                
if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [[1, 2, 1]]
    answers = [1]
    test(Solution().findMin, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)