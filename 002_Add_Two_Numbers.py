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
    
class Solution2(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1, p2 = l1, l2
        head = ListNode(0)
        prev, node = None, head
        while p1 or p2 or node.val >= 10:
            n1 = p1.val if p1 else 0
            n2 = p2.val if p2 else 0
            q, r = divmod(n1 + n2 + node.val, 10)
            node.val = r
            node.next = ListNode(q)
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
            prev, node = node, node.next
        if node.val == 0 and prev:
            prev.next = None
        return head

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    nums1 = [9, 9, 9]
    nums2 = [1]
    arguments = [(LinkedList(nums1).head, LinkedList(nums2).head)]
    answers = [[0, 0, 0, 1]]
    test(Solution2().addTwoNumbers, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)

