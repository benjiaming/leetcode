# Definition for singly-linked list.
#%%
class ListNode:
    def __init__(self, val=None):
        self.next = None
        if type(val) == list:
            if len(val) > 0:
                self.val = val.pop(0)
                self.next = ListNode(val)
            else:
                self.val = None
        else:
            self.val = val

    def add(self, val):
        if self.val is None:
            self.val = val
        else:
            while self.next is not None:
                self = self.next
            self.next = ListNode(val)

    @classmethod
    def traverse(cls, head):
        output = ''
        if head.val is not None:
            output = str(head.val)
        if head.next and head.next.val is not None:
            output += '->' + cls.traverse(head.next)
        return output


#%%
