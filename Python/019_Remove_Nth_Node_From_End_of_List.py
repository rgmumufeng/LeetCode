from leetcodelib import ListNode
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        
        fast = head
        for _ in xrange(n):
            fast = fast.next
        
        slow = dummy
        while fast:
            fast = fast.next
            slow = slow.next
            
        discarded = slow.next
        slow.next = discarded.next
        discarded.next = None

        return dummy.next
    
if __name__ == "__main__":
    from leetcodelib import LinkedList
    nums = range(1, 10)
    #n = len(nums)
    #n = 1
    n = 4
    answer = nums[:len(nums)-n] + nums[len(nums)-n+1:]
    testlist = LinkedList(nums)
    newhead = Solution().removeNthFromEnd(testlist.head, n)
    result = LinkedList().values(newhead)
    print answer
    print result
    print answer == result
    