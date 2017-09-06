import random
from solutions.leetcodelib import LinkedList

class Solution(object):
    def func1(self, nums):
        linkedlist = LinkedList(nums)
        return linkedlist.head
    
    def func2(self, ll):
        return random.sample(ll, len(ll))
        

if __name__ == "__main__":
    from solutions.leetcodelib import test
    nums1 = random.sample(range(20), 10)
    nums2 = [None] + nums1[1:]
    arguments = [nums1, nums2]
    answers = [nums1, nums1]
    test(Solution().func1, arguments, answers)
    test(Solution().func1, arguments, answers, inds=[0], mode='direct')
    print "func1 test finished.\n"
    

    l1 = [range(x) for x in random.sample(range(2, 10), 5)]
    while True:
        permutation = random.sample(l1[0], len(l1[0]))
        if permutation != l1[0]:
            break
    l2 = [permutation] + l1[1:]
    arguments = [l1, l1]
    answers = [l1, l2]
    test(Solution().func2, arguments, answers, mode='1D')
    test(Solution().func2, arguments, answers, inds=[1], mode='2D')
    print "func2 test finished.\n"
    

