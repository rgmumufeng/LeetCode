class Node(object):
        def __init__(self, k, v):
            self.label = k
            self.val = v
            self.prev = None
            self.next = None
            
        def __repr__(self):
            return "Node {} ({})".format(self.label, self.val)
            
class LRUCache(object):        
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.count = 0
        self.ref = {}
        self.head = Node(None, None)
        self.tail = self.head
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.find(key)
        return node.val if node else -1
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        node = self.find(key)
        if node:
            node.val = value
        else:
            if self.count == self.capacity:
                del self.ref[self.head.next.label]
                self.remove(self.head.next)
            else:
                self.count += 1
            node = Node(key, value)
            self.ref[key] = node
            self.append(node)
            
    def remove(self, node):
        node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.prev = node.next = None
        
    def append(self, node):
        node.prev, self.tail.next, self.tail = self.tail, node, node
                    
    def find(self, key):
        if key not in self.ref:
            return None
        node = self.ref[key]
        if node != self.tail:
            self.remove(node)
            self.append(node)
        return node
            
    def disp(self):
        print self.ref
        node = self.head.next
        while node:
            print node
            node = node.next
        print

if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.disp()
    cache.put(2, 2)
    cache.disp()
    cache.put(3, 3)
    cache.disp()
    print cache.get(2)
    cache.disp()
    cache.put(4, 4)
    cache.disp()
    print cache.get(1)
    cache.disp()
    print cache.get(3)
    cache.disp()
    print cache.get(4)  
    cache.disp()   