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
from list_node import ListNode

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

head = ListNode([1,1,2,2,2,3,3])
print(ListNode.traverse(head))
solution.deleteDuplicates(head)
print(ListNode.traverse(head))

print()

head = ListNode([1,1,1])
print(ListNode.traverse(head))
solution.deleteDuplicates(head)
print(ListNode.traverse(head))


#%%
