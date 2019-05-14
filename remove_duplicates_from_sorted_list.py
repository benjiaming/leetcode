"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2

Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
"""
#%%
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @classmethod
    def traverse(cls, head):
        output = str(head.val)
        if head.next:
            output += '->' + cls.traverse(head.next)
        return output


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """        
        if not head:
            return
        node = head.next
        prev = head
        while node:
            if node.val == prev.val:
                prev.next = node.next
            else:
                prev = node
            node = node.next
        return head

solution = Solution()

head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(2)
head.next.next.next.next.next = ListNode(3)
head.next.next.next.next.next.next = ListNode(3)
print(ListNode.traverse(head))
solution.deleteDuplicates(head)
print(ListNode.traverse(head))

print()

head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(1)
head.next.next.next = ListNode(1)
print(ListNode.traverse(head))
solution.deleteDuplicates(head)
print(ListNode.traverse(head))
