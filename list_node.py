# Definition for singly-linked list.
#%%
class ListNode:
    def __init__(self, val):
        self.next = None
        if type(val) in [str, int]: 
            self.val = val
        else:
            self.val = val.pop(0)
            if len(val):
                self.next = ListNode(val)


    @classmethod
    def traverse(cls, head):
        output = str(head.val)
        if head.next:
            output += '->' + cls.traverse(head.next)
        return output


#%%
