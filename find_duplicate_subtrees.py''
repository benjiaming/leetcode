# -*- coding: utf-8 -*-
"""
Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.

Example 1:

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4

The following are two duplicate subtrees:

      2
     /
    4

and

    4

Therefore, you need to return above trees' root in the form of a list.
"""
#%%
# Definition for a binary tree node.
from collections import Counter
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.val)
    def __repr__(self):
        return str(self.val)

class Solution(object):
    def findDuplicateSubtrees(self, root):
        result = []
        freq = Counter()

        def preorder_traversal(node):        
            if not node:
                return '#'
            path = [str(node.val)]
            path.append(preorder_traversal(node.left))
            path.append(preorder_traversal(node.right))
            serialized = ','.join(path)
            freq[serialized] += 1
            if freq[serialized] == 2:
                result.append(node)
            return serialized
        
        preorder_traversal(root)
        return result

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.right = TreeNode(3)
root.right.left = TreeNode(2)
root.right.left.left = TreeNode(4)
root.right.right = TreeNode(4)
solution = Solution()
print(solution.findDuplicateSubtrees(root))

