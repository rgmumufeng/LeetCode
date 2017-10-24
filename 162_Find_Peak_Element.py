class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = -int('inf')
        for i in xrange(len(nums)-1):
            if nums[i] > prev and nums[i] > nums[i+1]:
                return i
            prev = nums[i]
        return len(nums)-1
    
class Solution2(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.search(0, len(nums), nums)
        
    def search(self, i, j, nums):
        mid = (i+j)/2
        before = -float('inf') if mid == 0 else nums[mid-1]
        after = -float('inf') if mid == len(nums)-1 else nums[mid+1]
        left, right = mid-i, j-mid-1
        if nums[mid] > max(before, after):
            return mid
        elif before < nums[mid] < after or (nums[mid] < min(before, after) and right < left):
            return self.search(mid+1, j, nums)
        else:
            return self.search(i, mid, nums)
        
if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    #arguments = []
    #answers = []
    #test(Solution()., arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)