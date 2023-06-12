# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head):
        fast,slow=head,head
        while(fast and fast.next):
            fast=fast.next.next
            slow=slow.next
        return slow
    

# https://leetcode.com/problems/middle-of-the-linked-list/