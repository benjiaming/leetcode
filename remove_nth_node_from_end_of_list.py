"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
"""
#%%
from list_node import ListNode

class Solution(object):
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode

        Runs in O(L) where L is number of nodes in the ListNode
        """
        temp = ListNode(0)
        temp.next = head
        fast_pointer = temp
        slow_pointer = temp

        for _ in range(n):
            fast_pointer = fast_pointer.next

        while fast_pointer and fast_pointer.next:
            fast_pointer = fast_pointer.next
            slow_pointer = slow_pointer.next

        slow_pointer.next = slow_pointer.next.next

        return temp.next
