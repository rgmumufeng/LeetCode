class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        recent = [(nums[0], 0)] if nums[0] >= 0 else [(0, nums[0])]
        overall = [(x, y) for (x, y) in recent]
                    
        pos, neg = recent[-1]
        for i in xrange(1, len(nums)):
            tmp_pos = nums[i] if not pos else pos * nums[i]
            tmp_neg = 0 if not neg else neg * nums[i]
            pos, neg = (tmp_pos, tmp_neg) if nums[i] >= 0 else (tmp_neg, tmp_pos)

            recent.append((pos, neg))
            pos_all, neg_all = overall[-1]
            if pos and pos_all < pos:
                pos_all = pos
            if neg and neg_all > neg:
                neg_all = neg
            overall.append((pos_all, neg_all))
            #print recent, overall
        return overall[-1][0]
            
        

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [[0, 2], [2, 3, -2, 4], [-2, 0, -1]]
    answers = [2, 6, 0]
    test(Solution().maxProduct, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)