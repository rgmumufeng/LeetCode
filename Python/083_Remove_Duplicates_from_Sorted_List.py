from leetcodelib import ListNode, LinkedList
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        h, curr = head, head
        while curr.next:
            prev, curr = curr, curr.next
            if curr.val != prev.val:
                h.next = curr
                h = h.next
        h.next = None
        return head

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    nums1 = [1, 1, 2, 3, 3]
    arguments = [LinkedList(nums1).head]
    answers = [[1, 2, 3]]
    test(Solution().deleteDuplicates, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)