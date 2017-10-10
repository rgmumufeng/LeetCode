class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        for k in xrange(n):
            res = self.travel_once(n, k, gas, cost)
            if res >= 0:
                return res
        return 0 if n == 0 else -1
        
    def travel_once(self, n, k, gas, cost):
        storage = 0
        for i in xrange(n):
            j = i+k-n
            storage = storage + gas[j] - cost[j]
            if storage < 0:
                return -1
        return k
    
class Solution2(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if len(gas) == 0:
            return 0
        h = t = length = storage = 0
        while length < len(gas):
            if storage >= 0:
                storage += (gas[t] - cost[t])
                t += 1  
            else:
                h -= 1
                storage += (gas[h] - cost[h])
            length += 1
            
        return h % len(gas) if storage >= 0 else -1
                
            
        
        
    

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    #arguments = []
    #answers = []
    #test(Solution()., arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)