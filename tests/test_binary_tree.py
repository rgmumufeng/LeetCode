from solutions.leetcodelib import BinaryTree

def test_binary_tree():
    import time
    start_time = time.time()
    # Insert test functions below
    
    import numpy as np
    numbers = [2, 1, 3, 0, 7, 9, 1, 2, None, 1, 0, None, None, 8, 8, None, None, None, None, 7]
    
    tree1 = BinaryTree(numbers)
    tree1.write()

    if tree1.values() != numbers:
        print "generated linked list values not equal to original numbers"
        
    
    tree2 = BinaryTree(tree1.root.left)
    tree2.write()
    BinaryTree().write(tree1.root.left)
    
    print("Tests finished in %s seconds" % (time.time() - start_time))

if __name__ == "__main__":
    test_binary_tree()
