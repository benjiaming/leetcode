"""
Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node's value equals the given value. Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.

For example, 

Given the tree:
        4
       / \
      2   7
     / \
    1   3

And the value to search: 2

You should return this subtree:

      2     
     / \   
    1   3

In the example above, if we want to search the value 5, since there is no node with value 5, we should return NULL.

Note that an empty tree is represented by NULL, therefore you would see the expected output (serialized tree format) as [], not null.
"""
#%%
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @classmethod
    def _preorder(cls, node):
        output = []
        if node.left:
            output.extend(cls._preorder(node.left))
        output.append(str(node.val))
        if node.right:
            output.extend(cls._preorder(node.right))
        return output

    @classmethod
    def preorder(cls, node):
        return ' '.join(cls._preorder(node))

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return
        if root.val == val:
            return root
        elif root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
        

solution = Solution()
tree = TreeNode(4)
tree.left = TreeNode(2)
tree.left.left = TreeNode(1)
tree.left.right = TreeNode(3)
tree.right = TreeNode(7)
print(TreeNode.preorder(tree)) # 1 2 3 4 7

print(TreeNode.preorder(solution.searchBST(tree, 2))) # 1 2 3 