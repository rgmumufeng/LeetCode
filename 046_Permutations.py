class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """  
        groups = [[]]
        for num in nums:
            tmp = []
            for g in groups:
                for i in xrange(len(g)+1):
                    tmp.append(g[:i]+[num]+g[i:])
            groups = tmp
        return groups

if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    #nums = [1]
    result = Solution().permute(nums)
    print len(result)
    for x in result:
        print x