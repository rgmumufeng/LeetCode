from leetcodelib import ListNode, LinkedList

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        curr, ref, count = head, head.val, 1
        dummy = ListNode(None)
        h = dummy
        while curr.next:
            prev, curr = curr, curr.next
            if curr.val != ref:
                if count == 1:
                    h.next = prev
                    h = h.next
                    h.next = None
                ref = curr.val
                count = 1
            else:
                count += 1
        if count == 1:
            h.next = curr
        return dummy.next
                
if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    nums1 = [1, 2, 3, 3, 4, 4, 5]
    
    arguments = [LinkedList(nums1).head]
    answers = [[1, 2, 5]]
    test(Solution().deleteDuplicates, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)