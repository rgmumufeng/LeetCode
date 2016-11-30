class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        if len(nums) <3 or nums[0]*nums[-1] > 0:
            return ans

        for i in xrange(len(nums)-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r, left, right = i+1, len(nums)-1, None, None
            while l < r:
                if nums[l] == left or nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                elif nums[r] == right or nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    left, right = nums[l], nums[r]
                    l, r = l+1, r-1
        return ans
                        
                        
if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [[-1, 0, 1, 2, -1, -4], [0, 0, 0, 0], [1,-1,-1,0]]
    answers = [[[-1, 0, 1],[-1, -1, 2]], [[0, 0, 0]], [[-1,0,1]]]
    test(Solution().threeSum, arguments, answers, [1, 2])
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)