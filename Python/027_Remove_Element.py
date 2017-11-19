class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for j in xrange(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

if __name__ == "__main__":
    from leetcodelib import test
    arguments = [([1, 2, 3], 2), ([1, 1, 1, 3, 4], 1), ([2, 2, 2, 2, 2, 2, 2, 2, 2], 2), ([2 ,2 ,2], 3)]
    answers = [2, 2, 0, 3]
    test(Solution().removeElement, arguments, answers)