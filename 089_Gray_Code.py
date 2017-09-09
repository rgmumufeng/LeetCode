class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        dlt = [0, 1, 2, -1, 0]
        status = [1 for i in xrange((n+1)/2)]
        direction = [1 for i in xrange((n+1)/2)]
        
        def carry(ind):
            step = dlt[status[ind]]
            if step != 0:
                status[ind] += direction[ind]
                return ind, direction[ind] * step * 4 ** ind
            else:
                direction[ind] = -direction[ind]
                status[ind] += direction[ind]
                return carry(ind+1)
        
        answers = [0]
        for _ in xrange(2**n - 1):
            answers.append(answers[-1] + carry(0)[1])
        return answers
    
class Solution2(object):
    """
    Note that for Gray code, just reverse previous numbers with adding 1 in front, will
    natually keep the gray's rule.
    """ 
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        answers = [0, 1]
        for j in xrange(1, n):
            for i in xrange(len(answers)-1, -1, -1):
                answers.append(answers[i] + 2 ** j)
        return answers


if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [4, 6, 10]
    answers = [Solution2().grayCode(x) for x in arguments]
    test(Solution().grayCode, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)