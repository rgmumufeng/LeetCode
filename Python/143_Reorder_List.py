from leetcodelib import ListNode, LinkedList
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return head
        
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        prev, curr = None, slow.next
        slow.next = None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        
        node, next_node = head, prev
        while node:
            print node, next_node
            node.next, node, next_node = next_node, next_node, node.next
        return head
            
            

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    nums = [range(x) for x in xrange(1, 6)]
    arguments = [LinkedList(x).head for x in nums]
    answers = [[0], [0, 1], [0, 2, 1], [0, 3, 1, 2], [0, 4, 1, 3, 2]]
    test(Solution().reorderList, arguments, answers, inds=[3])
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)