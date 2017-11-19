class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        buy, sell, profit = prices[0], prices[0], 0
        for i in xrange(1, len(prices)):
            if prices[i] > sell:
                sell = prices[i]
                profit = max(profit, sell-buy)
            elif prices[i] > buy:
                continue
            else:
                buy = sell = prices[i]
        return profit

# Kadane's Algorithm    
class Solution2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxprof, currprof = 0, 0
        for i in xrange(1, len(prices)):
            currprof = max(0, currprof+prices[i]-prices[i-1])
            maxprof = max(currprof, maxprof)
        return maxprof
    

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [[7, 1, 5, 3, 6, 4], [7, 6, 4, 3, 1]]
    answers = [5, 0]
    test(Solution2().maxProfit, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)