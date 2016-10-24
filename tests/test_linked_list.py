from solutions.leetcodelib import LinkedList

def test():
    import time
    start_time = time.time()
    # Insert test functions below
    
    import numpy as np
    numbers = np.random.randint(1000, size=10000)
    list1 = LinkedList(numbers)
    list1.write()
    print list1
    print list1.head
    
    if np.any(list1.values() != numbers):
        print "generated linked list values not equal to original numbers"
        
    list2 = LinkedList(np.random.randint(1000, size=10))
    list2.write()
    LinkedList().write(list2.head)
    
    list3 = LinkedList()
    list3.write()
    print list3.head
    print("Tests finished in %s seconds" % (time.time() - start_time))

if __name__ == "__main__":
    test()
    