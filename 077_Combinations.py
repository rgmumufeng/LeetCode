class Solution1(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n<=0 or k <= 0:
            return [[]]
        
        nums = [x+1 for x in range(n)]
        if n == k:
            return [nums]
        
        if k > n-k:
            reverse, k = True, n-k
        else:
            reverse = False
            
        comb_list = [[x] for x in nums]
        for _ in xrange(1, k):
            tmp = []
            for l in comb_list:
                for x in nums[l[-1]:]:
                    tmp.append(l+[x])
            comb_list = tmp
            
        if reverse:
            numset = set(nums)
            tmp = []
            for l in comb_list:
                tmp.append(list(numset-set(l)))
            comb_list = tmp[::-1]
        
        return comb_list


class Solution(object):
    '''
    without using set(), can be applied to random list
    '''
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n<=0 or k <= 0:
            return [[]]
        
        if k > n-k:
            k = n-k
            flip = True
        else:
            flip = False
        
        masks = [([False for _ in xrange(n)], -1)]   
        for _ in xrange(k):
            tmp = []
            for m, i in masks:
                for x in range(i+1, n):
                    newm = list(m)
                    newm[x] = True
                    tmp.append((newm, x))
            masks = tmp
        
        masks, _ = zip(*masks)
        comb_list = []
        if flip:
            for m in masks:
                comb_list.append([i+1 for i, x in enumerate(m) if not x])
        else:
            for m in masks:
                comb_list.append([i+1 for i, x in enumerate(m) if x])
        return comb_list
            
        
            
                                     
                    

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [(4, 2), (4, 3)]
    answers = [[[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]],
               [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]]
        
    
               
    test(Solution().combine, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)