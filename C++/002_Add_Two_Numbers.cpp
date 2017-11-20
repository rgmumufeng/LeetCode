class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode dummy(0), *p = &dummy;
        int c=0;
        while (l1 || l2 || c) {
            int n = (l1 ? l1->val : 0) + (l2 ? l2->val : 0) + c;
            c = n / 10;
            p->next = new ListNode(n % 10);
            p = p->next;
            l1 = l1 ? l1->next : l1;
            l2 = l2 ? l2->next : l2;
        }
        return dummy.next;
    }
};


