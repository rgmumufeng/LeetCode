class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return False
        
        def rec(i, j, target):
            while j > i:
                mid = (i+j)/2
                if target == nums[mid]:
                    return True
                elif i+1 == j:
                    return False
                elif mid+1 == j or nums[i] <= target <= nums[mid-1]:
                    return rec(i, mid, target)
                elif nums[mid+1] <= target <= nums[j-1]:
                    return rec(mid+1, j, target)
                else:
                    return rec(i, mid, target) or rec(mid+1, j, target)
        return rec(0, len(nums), target)
        
        

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [([1,1,1,3,1], 3)]
    answers = [True]
    test(Solution().search, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)