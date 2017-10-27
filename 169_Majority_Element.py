class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ref = {}
        for n in nums:
            if n not in ref:
                ref[n] = 0
            if ref[n] == len(nums)/2:
                return n
            else:
                ref[n] += 1
                
# Solution 2 uses 'MJRTY - A Fast Majority Vote Algorithm' with O(1) space and O(n) time              
class Solution2(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for n in nums:
            if count == 0:
                maj = n
                count += 1
            elif n == maj:
                count += 1
            else:
                count -= 1
        return maj
                 

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    #arguments = []
    #answers = []
    #test(Solution()., arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)