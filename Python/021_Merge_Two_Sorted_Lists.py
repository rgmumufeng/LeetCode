from leetcodelib import ListNode
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(None)
        curr = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next, l1 = l1, l1.next
            else:
                curr.next, l2 = l2, l2.next
            curr = curr.next
            
        if not l1:
            curr.next = l2
        else:
            curr.next = l1
        return dummy.next

if __name__ == "__main__":
    from leetcodelib import LinkedList
    from random import sample
    nums1 = sorted(sample(range(100), 10))
    list1 = LinkedList(nums1)
    list1.write()
    
    nums2 = sorted(sample(range(100), 10))
    list2 = LinkedList(nums2)
    list2.write()
    
    nums_new = sorted(nums1 + nums2)
    list_new = LinkedList(nums_new)
    list_new.write()
    
    answer = LinkedList(nums_new).values()
    head_new = Solution().mergeTwoLists(list1.head, list2.head)
    result = LinkedList(head_new).values()
    
    print answer
    print result
    print answer == result
    