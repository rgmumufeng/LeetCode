class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 1:
            return 0
        
        area = sum(height)
        hts = sorted(list(enumerate(height)), key=lambda x: x[1], reverse=True)
        c, hc = hts[0]
        l, r = c, c
        empty = 0
        for x, hx in hts[1:]:
            if x < l:
                empty += (l-x)*(hc-hx)
                l = x
            elif x > r:
                empty += (x-r)*(hc-hx)
                r = x
            if l == 0 and r == len(height)-1:
                break
        return hc*len(height)-area-empty
        

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [[0,1,0,2,1,0,1,3,2,1,2,1]]
    answers = [6]
    test(Solution().trap, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)