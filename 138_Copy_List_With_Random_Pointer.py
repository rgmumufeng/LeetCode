class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        
        node = head
        while node:
            newnode = RandomListNode(node.label)
            node.next, newnode.next = newnode, node.next
            node = newnode.next
        newhead = head.next

        old = head
        while old:
            new = old.next
            new.random = None if not old.random else old.random.next
            old = new.next
        
        node = head
        while node and node.next:
            node.next, node = node.next.next, node.next
        
        return newhead    

def generate_list(n):
    import random
    numbers = range(n)
    nodes = [RandomListNode(x) for x in numbers]
    nodes.append(None)
    for i in xrange(n):
        nodes[i].next = nodes[i+1]
        nodes[i].random = random.choice(nodes)
    return nodes

def list_values(head):
    values = []
    while head:
        random_label = None if not head.random else head.random.label
        values.append((head.label, random_label))
        head = head.next
    return values

if __name__ == "__main__":
    n = 100
    head = generate_list(n)[0]
    ini = list_values(head)
    
    newhead = Solution().copyRandomList(head)
    
    print ini == list_values(head) == list_values(newhead)

        

