class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j = 0, len(nums)
        while i < j:
            mid = (i+j)/2
            if nums[mid] >= target:
                j = mid
            else:
                i = mid + 1
                
        if 0 <= i < len(nums) and nums[i] == target:
            left = i
        else:
            left = -1
            
        i, j = 0, len(nums)
        while i < j:
            mid = (i+j)/2
            if nums[mid] <= target:
                i = mid + 1
            else:
                j = mid
        if 0 <= j-1 <= len(nums) and nums[j-1] == target:
            right = j-1
        else:
            right = -1
            
        return [left, right]

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    #arguments = []
    #answers = []
    #test(Solution()., arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)