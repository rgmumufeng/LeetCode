# Solution 1 Brutal force
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        for i in xrange(len(nums)-1):
            for j in xrange(i+1, min(i+k+1, len(nums))):
                if abs(nums[j]-nums[i]) <= t:
                    return True
        return False

# Solution 2 use bucket
class Solution2(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 0 or t < 0:
            return False
        ref = {}
        for i in xrange(len(nums)):
            bucket = nums[i]/(t+1)
            if bucket in ref \
                or (bucket-1 in ref and abs(ref[bucket-1]-nums[i]) <= t) \
                or (bucket+1 in ref and abs(ref[bucket+1]-nums[i]) <= t):
                return True
            ref[bucket] = nums[i]
            if i >= k:
                del ref[nums[i-k]/(t+1)]
        return False


if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [([-1, -1], 1, -1)]
    answers = [False]
    test(Solution2().containsNearbyAlmostDuplicate, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)