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
        return root
    
class Solution2(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None

        prev, slow, fast = None, head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        right_head = slow.next

        root = TreeNode(slow.val)
        if not prev:
            root.left = None
        else:
            prev.next = None
            root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(right_head)
        return root
    
class Solution3(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        root = self.create_empty_tree(head)
        node, stack = root, []
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                node.val = head.val
                head = head.next
                node = node.right
        return root
        
    def create_empty_tree(self, head):
        if not head:
            return None
        root = TreeNode(None)
        level = [root]
        curr = head
        while True:
            tmp = []
            for node in level:
                if not curr.next:
                    return root
                node.left = TreeNode(None)
                tmp.append(node.left)
                curr = curr.next
                if not curr.next:
                    return root
                node.right = TreeNode(None)
                tmp.append(node.right)
                curr = curr.next
            level = tmp

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    nums_list = [range(100)]
    linkedlists = [LinkedList(x) for x in nums_list]
    arguments = [x.head for x in linkedlists]
    answers = nums_list
    test(Solution().sortedListToBST, arguments, answers, mode='inorder')
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)