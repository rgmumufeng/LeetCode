class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        count, farthest, can_reach = 0, 0, 0
        for i in xrange(len(nums)):
            if i > farthest:
                count += 1
                farthest = can_reach
            can_reach = max(can_reach, i+nums[i])
            if can_reach >= len(nums)-1:
                return count+1
        
if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [[2, 3, 1, 1, 4], [0], [1, 1, 1, 1], [1, 2, 1, 1, 1], [2, 0, 2, 0, 1]]
    answers = [2, 0, 3, 3, 2]
    test(Solution().jump, arguments, answers, [4])
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)