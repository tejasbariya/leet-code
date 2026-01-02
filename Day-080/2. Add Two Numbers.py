# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ''
        while l1 != None:
            num1 += str(l1.val)
            l1 = l1.next
        num2 = ''
        while l2 != None:
            num2 += str(l2.val)
            l2 = l2.next
        num1 = str(int(num1[::-1]) + int(num2[::-1]))
        values = [int(num) for num in num1][::-1]
        i = 0
        curr = ListNode(values[0])
        r = curr
        for i in range(1, len(values)):
            nextNode = ListNode(values[i])
            curr.next = nextNode
            curr = curr.next
        return r
