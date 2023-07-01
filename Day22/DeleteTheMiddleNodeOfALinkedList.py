# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head):
        if not head.next:
            return None
        slow=head
        fast=head.next.next
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        slow.next=slow.next.next

        return head
    

#https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/