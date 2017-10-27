from leetcodelib import ListNode, LinkedList
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k <= 1:
            #return head
            return LinkedList(head).values()

        dummy = ListNode(None)
        dummy.next = head
        gprev = dummy
        while gprev.next:
            tmp = gprev
            for i in xrange(k):
                tmp = tmp.next
                if not tmp:
                    #return dummy.next
                    return LinkedList(dummy.next).values()
            gtail, pc = gprev.next, gprev.next.next
            for i in xrange(k-1):
                gprev.next, pc.next, gtail.next = pc, gprev.next, pc.next
                pc = gtail.next
            gprev = gtail
        #return dummy.next
        return LinkedList(dummy.next).values()

class Solution2(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k <= 1:
            return head
        
        dummy = ListNode(None)
        dummy.next = head
        prev = dummy
        while True:
            h = prev
            for i in xrange(k):
                h = h.next
                if not h:
                    return dummy.next
            
            t = p = prev.next
            node = p.next
            for i in xrange(k-1):  
                next_node = node.next
                node.next, p, node = p, node, next_node
            prev.next, t.next = p, next_node
            prev = t
            
if __name__ == "__main__":
    from leetcodelib import test
    arguments = [(LinkedList(range(10)).head, i+1) for i in xrange(10)]
    answers = [range(10), 
               [1, 0, 3, 2, 5, 4, 7, 6, 9, 8], [2, 1, 0, 5, 4, 3, 8, 7, 6, 9],
               [3, 2, 1, 0, 7, 6, 5, 4, 8, 9], [4, 3, 2, 1, 0, 9, 8, 7, 6, 5],
               [5, 4, 3, 2, 1, 0, 6, 7, 8, 9], [6, 5, 4, 3, 2, 1, 0, 7, 8, 9],
               [7, 6, 5, 4, 3, 2, 1, 0, 8, 9], [8, 7, 6, 5, 4, 3, 2, 1, 0, 9],
               [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]]
    test(Solution2().reverseKGroup, arguments, answers, inds=[])