class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if not denominator:
            return ""
            
        symbol = "-" if numerator/denominator < 0 else ""
        numerator, denominator = abs(numerator), abs(denominator)
        
        int_part, x = divmod(numerator, denominator)
        if not x:
            return symbol + str(int_part)
        
        nums, ref, i = [int_part, "."], {}, 2
        while x and x not in ref:
            ref[x] = i
            n, x = divmod(x*10, denominator)
            nums.append(n)
            i += 1
        
        if not x:
            return symbol + "".join([str(x) for x in nums])
        else:
            j = ref[x]
            return symbol + "".join([str(x) for x in nums[:j]]) + "(" + \
                "".join([str(x) for x in nums[j:]]) + ")"
            

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [(1, 2), (2, 1), (2, 3), (1, 90), (-50, 8), (0, -5)]
    answers = ["0.5", "2", "0.(6)", "0.0(1)", "-6.25", "0"]
    test(Solution().fractionToDecimal, arguments, answers, inds=None)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)