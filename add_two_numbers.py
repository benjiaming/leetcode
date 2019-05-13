You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        print(self.val)

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        carry = 0
        p = l1
        q = l2
        dummyHead = ListNode(0)
        curr = dummyHead
        
        while (p != None or q != None):
            x = p.val if p else 0
            y = q.val if q else 0
            total = carry + x + y
            carry = total / 10
            curr.next = ListNode(total % 10)
            curr = curr.next
            if p is not None:
                p = p.next
            if q is not None:
                q = q.next
        
        if carry > 0:
            curr.next = ListNode(carry)
        
        return dummyHead.next
    
            
