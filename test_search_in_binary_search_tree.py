import unittest
from search_in_binary_search_tree import Solution, TreeNode

class TestSolution(unittest.TestCase):
   def test_search_in_binary_search_tree(self):
       solution = Solution()
       tree = TreeNode(4)
       tree.left = TreeNode(2)
       tree.left.left = TreeNode(1)
       tree.left.right = TreeNode(3)
       tree.right = TreeNode(7)
       self.assertEqual(TreeNode.preorder(tree), '1 2 3 4 7')
       node = solution.searchBST(tree, 2)
       self.assertEqual(TreeNode.preorder(node), '1 2 3')
       node = solution.searchBST(tree, 5)
       self.assertIsNone(node)  

if __name__ == '__main__':
    unittest.main()