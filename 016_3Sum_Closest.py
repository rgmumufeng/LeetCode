class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        if len(nums) < 3:
            return None
        
        ans = None
        for i in xrange(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l, r = i+1, len(nums)-1
            while l < r:             
                tmp = nums[i] + nums[l] + nums[r]
                if tmp == target:
                    return target
                
                if tmp > target:
                    r -= 1
                else:
                    l += 1
                    
                if ans == None or abs(tmp-target) < abs(ans-target):
                    ans = tmp
        return ans
                
class Solution2(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = nums[0]+nums[1]+nums[2]
        for i in xrange(len(nums)-2):
            if i == 0 or nums[i] != nums[i-1]:
                h, t = i+1, len(nums)-1
                while h < t:
                    tmp = nums[h]+nums[t]+nums[i]
                    if tmp == target:
                        return target
                    if tmp > target:
                        t -= 1
                    elif tmp < target:
                        h += 1
                    res = tmp if abs(target-tmp) < abs(target-res) else res
        return res
                
            
        

            
if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [([-1, 2, 1, -4], 1), ([0, 0, 0], 1), ([87,6,-100,-19,10,-8,-58,56,14,-1,-42,-45,-17,10,20,-4,13,-17,0,11,-44,65,74,-48,30,-91,13,-53,76,-69,-19,-69,16,78,-56,27,41,67,-79,-2,30,-13,-60,39,95,64,-12,45,-52,45,-44,73,97,100,-19,-16,-26,58,-61,53,70,1,-83,11,-35,-7,61,30,17,98,29,52,75,-73,-73,-23,-75,91,3,-57,91,50,42,74,-7,62,17,-91,55,94,-21,-36,73,19,-61,-82,73,1,-10,-40,11,54,-81,20,40,-29,96,89,57,10,-16,-34,-56,69,76,49,76,82,80,58,-47,12,17,77,-75,-24,11,-45,60,65,55,-89,49,-19,4], -275)]
    answers = [2, 0, -274]
    test(Solution2().threeSumClosest, arguments, answers, [])
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)