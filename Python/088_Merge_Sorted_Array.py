class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i, j, curr = m-1, n-1, m+n-1
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[curr] = nums1[i]
                i -= 1
            else:
                nums1[curr] = nums2[j]
                j -= 1
            curr -= 1

        if j >= 0:
            nums1[:j+1] = nums2[:j+1]
        return nums1
            
            

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    from random import sample
    
    def verify(nums1, m, nums2, n):
        return sorted(nums1[:m]+nums2[:n])
    
    def create(m, n):
        return sorted(sample(range(100), m+n)), m, sorted(sample(range(100), n)), n
    
    arguments = [create(5, 10), create(10, 5)]
    answers = [verify(*arg) for arg in arguments]
    test(Solution().merge, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)