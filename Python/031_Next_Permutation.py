class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return nums

        i = len(nums)-1
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1
       
        if i > 0:
            j = i
            while j < len(nums) and nums[j] > nums[i-1]:
                j += 1
            nums[i-1], nums[j-1] = nums[j-1], nums[i-1]
        
        j = len(nums)-1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        return nums
        

if __name__ == "__main__":
    from leetcodelib import test
    arguments = [[1, 2, 3], [3, 2, 1], [1, 1, 5], [3, 7, 4, 3, 5, 4, 2, 1]]
    answers = [[1, 3, 2], [1, 2, 3], [1, 5, 1], [3, 7, 4, 4, 1, 2, 3, 5]]
    
    test(Solution().nextPermutation, arguments, answers)
    