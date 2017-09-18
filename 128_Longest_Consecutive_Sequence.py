class Solution(object):
    '''
    this is a copy of StefanPochmann's solution from:
    https://discuss.leetcode.com/topic/15383/simple-o-n-with-explanation-just-walk-each-streak
    '''
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        best = 0
        for x in nums:
            if x-1 not in nums:
                y = x+1
                while y in nums:
                    y += 1
                best = max(best, y-x)
        return best
    
class Solution2(object):
    '''
    this is a variation of dchen0215's solution from:
    https://discuss.leetcode.com/topic/6148/my-really-simple-java-o-n-solution-accepted
    '''
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        records = {}
        best = 0
        for x in nums:
            if x not in records:
                left = records.get(x-1, 0)
                right = records.get(x+1, 0)
                length = left+right+1
                records[x] = records[x-left] = records[x+right] = length
                best = max(best, length)
        return best
                
                

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [[100, 4, 200, 1, 3, 2]]
    answers = [4]
    test(Solution2().longestConsecutive, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)