from leetcodelib import ListNode, LinkedList
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        
        prev, node = None, head
        while node:
            next_node = node.next
            node.next = prev
            prev, node = node, next_node
        return prev
    
class Solution2(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        new_head = self.reverseList(head.next)
        head.next.next, head.next = head, None
        return new_head

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [LinkedList([1, 2]).head]
    answers = [[2, 1]]
    test(Solution2().reverseList, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)