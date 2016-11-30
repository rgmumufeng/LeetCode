from leetcodelib import ListNode, TreeNode, LinkedList, BinaryTree

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def helper(node, n):
            if n == 0:
                return None, None
            if n == 1:
                return TreeNode(node.val), node
            n1 = n/2
            n2 = n1 if n%2==1 else n1-1
            hleft, node = helper(node, n1)
            node = node.next
            root, root_in_list = TreeNode(node.val), node
            root.left = hleft
            node = node.next
            hright, node = helper(node, n2)
            root.right = hright
            node = node if node else root_in_list
            return root, node

        p = head
        count = 0
        while p:
            count += 1
            p = p.next
        root = helper(head, count)[0]
        #return root
        return BinaryTree(root).inorder()

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    nums_list = [range(100)]
    linkedlists = [LinkedList(x) for x in nums_list]
    arguments = [x.head for x in linkedlists]
    answers = nums_list
    test(Solution().sortedListToBST, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)