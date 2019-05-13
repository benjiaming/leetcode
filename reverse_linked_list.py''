# -*- coding: utf-8 -*-
"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
#%%
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        node = head
        while node is not None:
            swap = node.next
            node.next = prev
            prev = node
            node = swap
        return prev


    def traverse(self, head):
        output = [str(head.val)]
        node = head.next
        while node is not None:
            output.append(str(node.val))
            node = node.next
        return '->'.join(output)

solution = Solution()

node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)
node.next.next.next.next = ListNode(5)
print(solution.traverse(node))

new_node = solution.reverseList(node)
print(solution.traverse(new_node))



 #%%


#%%
