class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        totprof, currprof = 0, 0
        for i in xrange(1, len(prices)):
            prof_today = prices[i]-prices[i-1]
            if prof_today >= 0:
                currprof += prof_today
            else:
                totprof += currprof
                currprof = 0
        return totprof+currprof
    
class Solution2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        totprof = 0
        for i in xrange(1, len(prices)):
            today_prof = prices[i]-prices[i-1]
            if today_prof > 0:
                totprof += today_prof
        return totprof

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    #arguments = []
    #answers = []
    #test(Solution()., arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)