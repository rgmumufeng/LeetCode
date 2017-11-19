class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        nums.sort()
        res = []
        for i in xrange(len(nums)-3):
            if i == 0 or nums[i] != nums[i-1]:
                for j in xrange(i+1, len(nums)-2):
                    if j == i+1 or nums[j] != nums[j-1]:
                        h, t = j+1, len(nums)-1
                        while h < t:
                            tmp = nums[i]+nums[j]+nums[h]+nums[t]
                            if tmp > target:
                                t -= 1
                            elif tmp < target:
                                h += 1
                            else:
                                res.append([nums[i], nums[j], nums[h], nums[t]])
                                while h < t-1 and nums[t-1] == nums[t]:
                                    t -= 1
                                while h+1 < t and nums[h+1] == nums[h]:
                                    h += 1
                                h, t = h+1, t-1
        return res

# Solution 2: general solution to find n-sum
class Solution2(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return self.nsum(sorted(nums), 0, target, 4)
    
    def nsum(self, nums, start, target, n):
        if len(nums)-start < n:
            return []
        res= []
        if n == 2:
            h, t = start, len(nums)-1
            while h < t:
                #print 'target', target, '?', nums[h], nums[t]
                if nums[h]*2 > target or nums[t]*2 < target:
                    #print 'out of range', nums[h]*2, target, nums[t]*2
                    break
                if nums[h] + nums[t] < target:
                    h += 1
                elif nums[h] + nums[t] > target:
                    t -= 1
                else:
                    res.append([nums[h], nums[t]])
                    while h+1 < t and nums[h+1] == nums[h]:
                        h += 1
                    while h < t-1 and nums[t-1] == nums[t]:
                        t -= 1
                    h, t = h+1, t-1
        else:
            for i in xrange(start, len(nums)-n+1):
                if i == start or nums[i] != nums[i-1]:
                    res.extend([nums[i]]+x for x in self.nsum(nums, i+1, target-nums[i], n-1))
        return res
                
        
        
if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [([1, 0, -1, 0, -2, 2], 0)]
    answers = [[[-1,  0, 0, 1],[-2, -1, 1, 2],[-2,  0, 0, 2]]]
    test(Solution2().fourSum, arguments, answers, mode='1D')
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)