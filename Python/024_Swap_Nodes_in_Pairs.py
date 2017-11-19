from leetcodelib import ListNode, LinkedList
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            #return head
            return None if not head else [head.val]
        
        dummy = ListNode(None)
        dummy.next = head
        prev, left, right = dummy, head, head.next
        while left and right:
            pnext = right.next
            prev.next, right.next, left.next = right, left, right.next
            prev, left = left, pnext
            right = left.next if left else None
        #return dummy.next
        return LinkedList(dummy.next).values()

class Solution2(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        prev = dummy
        while prev.next and prev.next.next:
            first, second = prev.next, prev.next.next
            prev.next, second.next, first.next = second, first, second.next
            prev = first
        return dummy.next

if __name__ == "__main__":
    from leetcodelib import test
    num_lists = [[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]
    arguments = [LinkedList(nums).head for nums in num_lists]
    answers = [None, [0], [1, 0], [1, 0, 2], [1, 0, 3, 2]]
    test(Solution2().swapPairs, arguments, answers)