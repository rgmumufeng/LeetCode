# Solution 1: brute force
class Solution(object):
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
        ref = {}
        for i in xrange(len(nums)):
            if nums[i] in ref:
                return [ref[nums[i]], i]
            else:
                ref[target-nums[i]] = i
                

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [([2, 7, 11, 15], 9), ([3, 2, 4], 6)]
    answers = [[0, 1], [1, 2]]
    test(Solution2().twoSum, arguments, answers)
     
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)
    
    

