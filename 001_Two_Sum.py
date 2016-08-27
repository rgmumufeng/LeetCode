# Solution 1: brute force
class Solution1(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in xrange(len(nums)-1):
            for j in xrange(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return sorted([i, j])     

# Solution 2: hashmap
class Solution2(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, n in enumerate(nums):
            if n in d.keys():
                return sorted([i, d[n]])
            else:
                d[target-n] = i   

if __name__ == "__main__":
    from leetcodelib import test
    arguments = [([2, 7, 11, 15], 9)]
    answers = [[0, 1]]
    test(Solution1().twoSum, arguments, answers)
    test(Solution2().twoSum, arguments, answers)
    

