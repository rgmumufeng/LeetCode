from leetcodelib import ListNode, LinkedList
class Solution1(object):
    # Time Limit Exceeded
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        lists = [p for p in lists if p]
        if not lists:
            return None
        values = [p.val for p in lists]
        dummy = ListNode(None)
        curr = dummy
        while len(lists) > 1:
            ind = values.index(min(values))
            curr.next = lists[ind]
            curr = curr.next
            if not lists[ind].next:
                lists.pop(ind)
                values.pop(ind)
            else:
                lists[ind] = lists[ind].next
                values[ind] = lists[ind].val
        curr.next = lists[0]
        #return dummy.next
        return LinkedList(dummy.next).values() 


class Solution2(object):
    # Time Limit Exceeded
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def mergetwo(l1, l2):
            dummy = ListNode(None)
            curr = dummy
            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next, l1 = l1, l1.next
                else:
                    curr.next, l2 = l2, l2.next
                curr = curr.next
            
            if not l1:
                curr.next = l2
            else:
                curr.next = l1
            return dummy.next
        
        #print 'here'
        if not list:
            return None
        while len(lists) > 1:
            #print 'here'
            newhead = mergetwo(lists.pop(), lists.pop())
            #print newhead.val
            lists.append(newhead)       
        #return lists[0]
        return LinkedList(lists[0]).values() 

    
class Solution3(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head_values = sorted([(p, p.val) for p in lists if p], key=lambda x: x[1], reverse=True)
        if not head_values:
            return None
        
        dummy = ListNode(None)
        curr = dummy
        while len(head_values) > 1:
            if head_values[-1][1] <= head_values[-2][1]:
                curr.next = head_values[-1][0]
                curr = curr.next
                if head_values[-1][0].next:
                    head_values[-1] = (head_values[-1][0].next, head_values[-1][0].next.val)
                else:
                    head_values.pop()
            else:
                head_values.sort(key=lambda x: x[1], reverse=True)
                
        curr.next = head_values[0][0]
        #return dummy.next
        return LinkedList(dummy.next).values()    

if __name__ == "__main__":
    from leetcodelib import test, update_testfile
    from random import sample, randint
    import yaml
    
    testfile = __file__.replace('.py', '.yaml')
    
    #arg_names = 'num_lists'
    #k = randint(1, 20)
    #args = [sorted(sample(range(100), randint(1, 10))) for _ in xrange(k)]
    #answer = sorted([x for l in args for x in l])
    #update_testfile(testfile, arg_names, [(args,)], [answer])

    with open(testfile, 'r') as f:
        data = yaml.safe_load(f)
        arg_orders = data[0]['argument_orders']
        test_cases = data[1:]
        
    arguments, answers = [], []
    arg_name = arg_orders[0]
    
    test_lists = [case['input_args'][arg_name] for case in test_cases]
    arguments = [[LinkedList(x).head for x in lists] for lists in test_lists]
    answers = [case['output_answer'] for case in test_cases]
    
    test(Solution1().mergeKLists, [[LinkedList(x).head for x in lists] for lists in test_lists], answers)
    test(Solution2().mergeKLists, [[LinkedList(x).head for x in lists] for lists in test_lists], answers)
    test(Solution3().mergeKLists, [[LinkedList(x).head for x in lists] for lists in test_lists], answers)
    