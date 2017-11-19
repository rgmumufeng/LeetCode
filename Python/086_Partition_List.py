from leetcodelib import ListNode, LinkedList

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        small = dummy_small = ListNode(None)
        large = dummy_large = ListNode(None)
             
        node = head
        while node:
            if node.val < x:
                small.next = node
                small = small.next
            else:
                large.next = node
                large = large.next
            node = node.next
        
        small.next = dummy_large.next
        large.next = None
        return dummy_small.next

if __name__ == "__main__":
    import numpy as np
    numbers, x = np.random.randint(10, size=20), 5
    #numbers, x = [5] * 20, 5
    #numbers, x = [4] * 20, 5
    #numbers, x = [2, 1], 3
    testlist = LinkedList(numbers)
    testlist.write()

    head = Solution().partition(testlist.head, x)
    LinkedList().write(head)
    

