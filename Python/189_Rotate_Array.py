class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        while k >= len(nums):
            k %= len(nums)
        for _ in xrange(k):
            self.shift(nums)
        return nums
        
    def shift(self, nums):
        tmp = nums[-1]
        for i in xrange(len(nums)):
            nums[i], tmp = tmp, nums[i]
            
class Solution2(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        while k >= len(nums):
            k %= len(nums)
        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums)-1)
        return nums
        
    def reverse(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [(range(10), 3), (range(10), 17)]
    answers = [[7,8,9,0,1,2,3,4,5,6], [3,4,5,6,7,8,9,0,1,2]]
    test(Solution2().rotate, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)