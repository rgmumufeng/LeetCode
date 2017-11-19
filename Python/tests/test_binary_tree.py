from leetcodelib import BinaryTree

def test_binary_tree():
    import time
    start_time = time.time()
    # Insert test functions below
    
    import numpy as np
    numbers = [2, 1, 3, 0, 7, 9, 1, 2, None, 1, 0, None, None, 8, 8, None, None, None, None, 7]
    
#  tree1
#                  2
#          1               3
#      0       7       9       1
#    2       1   0           8   8
#               7 

    tree1 = BinaryTree(numbers)
    tree1.write()

    if tree1.values() != numbers:
        print "generated linked list values not equal to original numbers"
    
    inorder = [2, 0, 1, 1, 7, 7, 0, 2, 9, 3, 8, 1, 8]
    print "inorder", inorder
    print "check inorder", tree1.inorder() == inorder
    print "check morris_inorder", tree1.morris_inorder() == inorder
    
    preorder = [2, 1, 0, 2, 7, 1, 0, 7, 3, 9, 1, 8, 8]
    print "preorder", preorder
    print "check preorder", tree1.preorder() == preorder
    print "check morris_preorder", tree1.morris_preorder() == preorder
    
    postorder = [2, 0, 1, 7, 0, 7, 1, 9, 8, 8, 1, 3, 2]
    print "postorder", postorder
    print "check postorder", tree1.postorder() == postorder

    tree2 = BinaryTree(tree1.root.left)
    tree2.write()
    BinaryTree().write(tree1.root.left)
    
    
    
    print("Tests finished in %s seconds" % (time.time() - start_time))

if __name__ == "__main__":
    test_binary_tree()
