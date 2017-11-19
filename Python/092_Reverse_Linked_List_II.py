from leetcodelib import ListNode, LinkedList

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next or m == n:
            return head
        
        dummy = ListNode(None)
        dummy.next = head
        prev = dummy
        for _ in xrange(m-1):
            prev = prev.next
        curr = prev.next    
        
        revprev, revhead = prev, curr
        prev, curr = curr, curr.next
        
        for _ in xrange(n-m):
            curr.next, prev, curr = prev, curr, curr.next

        revhead.next = curr
        revprev.next = prev
        return dummy.next
        

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    from random import sample
    
    def verify(nums, m, n):
        m -= 1
        n -= 1
        return nums[:m] + nums[n:m-1:-1] + nums[n+1:]

    l = sample(range(100), 20)
    print l
    arguments = [(LinkedList(l).head, 3, 15)]
    answers = [verify(l, x[1], x[2]) for x in arguments]
    test(Solution().reverseBetween, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)