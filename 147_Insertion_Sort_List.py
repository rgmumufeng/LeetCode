from leetcodelib import ListNode, LinkedList
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        curr, foll = head, head.next
        curr.next = None
        while foll:
            tmp = foll.next
            if foll.val <= curr.val:
                foll.next, curr = curr, foll
            else:
                c = curr
                while c.next and foll.val > c.next.val:
                    c = c.next
                c.next, foll.next = foll, c.next
            foll = tmp
        return curr
                
            
        

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    nums = [[3, 2, 4]]
    arguments = [LinkedList(x).head for x in nums]
    answers = [sorted(x) for x in nums]
    test(Solution().insertionSortList, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)