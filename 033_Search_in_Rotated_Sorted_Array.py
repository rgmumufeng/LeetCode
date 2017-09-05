class Solution1(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """        
        def find_head():
            i, j = 0, len(nums)
            while i < j:
                mid = (i+j)/2
                if nums[mid] < nums[i]:
                    if mid-1 >= 0 and nums[mid-1] > nums[mid]:
                        return mid
                    else:
                        j = mid+1
                elif mid+1 < len(nums) and nums[mid+1] < nums[mid]:
                    return mid+1
                else:
                    i = mid+1
            return 0
                    
        def find_target(i0, j0, t):
            i, j = i0, j0
            while i < j:
                mid = (i+j)/2
                if nums[mid] == t:
                    return mid
                elif nums[mid] < t:
                    i = mid+1
                else:
                    j = mid
            return -1
        
        h = find_head()       
        if h == 0:
            return find_target(0, len(nums), target)
        
        if target == nums[0]:
            return 0
        elif target < nums[0]:
            return find_target(h, len(nums), target)
        else:
            return find_target(0, h, target)

class Solution2(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i, j = 0, len(nums)
        while j-i>1:
            mid = (i+j-1)/2
            if nums[mid] > nums[j-1]:
                i = mid+1
            else:
                j = mid+1
        #print 'head is', nums[i]
        
        if target == nums[-1]:
            return len(nums)-1
        if target > nums[-1]:
            i, j = 0, i
        else:
            i, j = i, len(nums)
        #print 'check in', nums[i:j]

        while i < j:
            mid = (i+j)/2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                i = mid+1
            else:
                j = mid
        return -1
            
                       
def find_head(nums):
    i, j = 0, len(nums)
    
    while j-i>1:
        mid = (i+j-1)/2
        print "check", nums[mid],
        if nums[mid] > nums[j-1]:
            i = mid+1
        else:
            j = mid+1
        print 'search in', nums[i:j]
    return i


class Solution3(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        
        def recursive(i, j, target):
            if j-i == 1:
                return i if target == nums[i] else -1
            else:
                mid = (i+j)/2
                if (nums[i] <= target <= nums[mid-1]) \
                    or target < nums[mid] <= nums[j-1] \
                    or nums[mid] <= nums[j-1] < target:
                    return recursive(i, mid, target)
                else:
                    return recursive(mid, j, target)
        return recursive(0, len(nums), target)
        
        
class Solution4(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        
        i, j = 0, len(nums)
        while j-i > 1:
            mid = (i+j)/2
            if nums[i] <= target <= nums[mid-1] \
            or target < nums[mid] <= nums[j-1] \
            or nums[mid] <= nums[j-1] < target:
                j = mid
            else:
                i = mid
        
        return i if  nums[i] == target else -1
        
            
        

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [([1, 3], 3), ([5, 1, 3], 1), ([3, 1], 3)]
    answers = [1, 1, 0]
    test(Solution4().search, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)
    
    #n = 8
    #l = range(n)
    #for i in xrange(n):
    #    ll = l[i:] + l[0:i]
    #    print ll
    #    print ll[find_head(ll)]
    

