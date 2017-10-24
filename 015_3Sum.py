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
                        

class Solution2(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        print nums
        res = []
        for i in xrange(len(nums)-2):
            if i == 0 or nums[i] != nums[i-1]:
                h, t = i+1, len(nums)-1
                print i, h, t, nums[i], nums[h], nums[t]
                while h < t:
                    if nums[h] + nums[t] < -nums[i]:
                        h += 1
                    elif nums[h] + nums[t] > -nums[i]:
                        t -= 1
                    else:
                        res.append([nums[i], nums[h], nums[t]])
                        h, t = h+1, t-1
                        print res, h, t, nums[h], nums[t]
                        while h < t and nums[h] == nums[h-1]:
                            h += 1
                        while h < t and nums[t] == nums[t+1]:
                            t -= 1
        return res
               
if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [[-1, 0, 1, 2, -1, -4], [0, 0, 0, 0], [1,-1,-1,0], [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0], [-2,0,1,1,2]]
    answers = [[[-1, 0, 1],[-1, -1, 2]], [[0, 0, 0]], [[-1,0,1]], [[-5,1,4],[-4,0,4],[-4,1,3],[-2,-2,4],[-2,1,1],[0,0,0]], [[-2,0,2],[-2,1,1]]]
    test(Solution2().threeSum, arguments, answers, inds=[-1], mode='1D')
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)