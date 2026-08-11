# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode()
        dummy.next = head
        A = dummy
        B = dummy
        for i in range(n+1):
            A = A.next
        while A:
            B = B.next
            A = A.next
        B.next = B.next.next
        return dummy.next        
        