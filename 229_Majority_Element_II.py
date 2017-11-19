class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ref = {}
        res = set()
        for n in nums:
            if n not in ref:
                ref[n] = 0
            ref[n] += 1
            if ref[n] > len(nums)/3 and n not in res:
                res.add(n)
        return list(res)

    
class Solution2(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        n1, n2, c1, c2 = None, None, 0, 0
        for n in nums:
            if n == n1:
                c1 += 1
            elif n == n2:
                c2 += 1
            elif c1 == 0:
                n1, c1 = n, 1
            elif c2 == 0:
                n2, c2 = n, 1
            else:
                c1 -= 1
                c2 -= 1
        return [x for x in [n1, n2] if nums.count(x) > len(nums)/3]
            

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [[1, 2]]
    answers = [[1, 2]]
    test(Solution2().majorityElement, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)