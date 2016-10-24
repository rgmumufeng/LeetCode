class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        
        i = 0
        for j in xrange(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i+1

if __name__ == "__main__":
    from leetcodelib import test
    arguments = [[1, 2, 3], [1, 1, 2, 3, 4], [1, 2, 3, 3, 4, 5, 5, 6, 6]]
    answers = [3, 4, 6]
    test(Solution().removeDuplicates, arguments, answers)