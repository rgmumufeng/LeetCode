class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums
        
        i, red = 0, None
        while i < len(nums):
            if nums[i] == 0:
                i += 1
            else:
                red = i
                break
        if red == None:
            return nums
        
        i, blue = len(nums)-1, None
        while i >= 0:
            if nums[i] == 2:
                i -= 1
            else:
                blue = i
                break
        if blue == None:
            return nums
        
        #print red, blue
        p = red
        while p <= blue:
            if nums[p] == 2:
                nums[p], nums[blue] = nums[blue], nums[p]
                blue -= 1
            else:
                if nums[p] == 0:
                    nums[p], nums[red] = nums[red], nums[p]
                    red += 1
                p += 1
        return nums


if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [[0, 1, 2, 2, 1, 0, 0, 1, 0, 2, 1], [1, 0]]
    answers = [sorted(x) for x in arguments]
    test(Solution().sortColors, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)