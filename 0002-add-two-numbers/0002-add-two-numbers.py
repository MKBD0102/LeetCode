# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        now1 = l1
        now2 = l2

        val1 = 0; i = 0
        val2 = 0; j = 0

        while now1:
            val1 += now1.val * (10**i)
            now1 = now1.next
            i += 1

        while now2:
            val2 += now2.val * (10**j)
            now2 = now2.next
            j += 1
        
        fin = val1+val2
        current=ListNode(fin%10)
        fin = fin//10
        res = current
        while fin > 0:
            new = ListNode(fin%10)
            current.next = new
            current = current.next
            fin = fin//10
        return res