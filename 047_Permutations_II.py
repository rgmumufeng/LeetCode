class Solution1(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        
        checked, permuted = [], []
        for i, num in enumerate(nums):
            if num  not in checked:
                for p in self.permuteUnique(nums[:i]+nums[i+1:]):
                    permuted.append([num]+p)
                checked.append(num)
        return permuted
    
# Solution2 is a copy of StefanPochmann's solution from 
# https://discuss.leetcode.com/topic/32976/9-line-python-solution-with-1-line-to-handle-duplication-beat-99-of-others/2
class Solution2(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        for n in nums:
            ans = [l[:i]+[n]+l[i:]
                   for l in ans
                   for i in xrange((l+[n]).index(n)+1)]
            return ans

if __name__ == "__main__":
    #from leetcodelib import test
    arguments = [1, 1, 2, 3, 4, 4]
    #answers = []
    #test(Solution()., arguments, answers)
    result1 = Solution1().permuteUnique(arguments).sort()
    result2 = Solution1().permuteUnique(arguments).sort()
    print result1 == result2
    