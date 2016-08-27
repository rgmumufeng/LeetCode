from leetcodelib import ListNode, LinkedList

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        prev = dummy = ListNode(None)
        node1, node2, c = l1, l2, 0
        while node1 or node2:
            n1, node1 = (node1.val, node1.next) if node1 else (0, None)
            n2, node2 = (node2.val, node2.next) if node2 else (0, None)
            c, val = divmod(n1+n2+c, 10)
            prev.next = ListNode(val)
            prev = prev.next
        if c:
            prev.next = ListNode(c)
            
        return dummy.next

if __name__ == "__main__":
    nums1, nums2 = [9, 9, 9], [1]
    list1, list2 = LinkedList(nums1), LinkedList(nums2)
    head = Solution().addTwoNumbers(list1.head, list2.head)
    LinkedList().write(head)

