class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """      
        ref = [[{} for _ in xrange(i+1)] for i in xrange(9)]
        return self.calculate(9, k, n, ref)
    
    def lower(self, k):
        return k*(k+1)/2
    
    def upper(self, i, k):
        return (2*i-k+1)*k/2
    
    def calculate(self, i, k, n, ref):
        if n < self.lower(k) or n > self.upper(i, k):
            return []
        
        if n not in ref[i-1][k-1]:
            res = []
            if k == 1 and n <= i:
                res = [[n]]
            elif k > 1:
                num = i
                while n-num <= self.upper(num-1, k-1):
                    for x in self.calculate(num-1, k-1, n-num, ref):
                        res.append([num]+x)
                    num -= 1
        #print "target {} ? sum of {} numbers with max of {}".format(n, k, i), res
            ref[i-1][k-1][n] = res
        return ref[i-1][k-1][n]
        
                
                    

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [(3, 7), (3, 9), (3, 2)]
    answers = [[[1, 2, 4]], [[1,2,6], [1,3,5], [2,3,4]], []]
    test(Solution().combinationSum3, arguments, answers, inds=[], mode='2D')
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)