import unittest
from validate_binary_search_tree import Solution, TreeNode

class TestSolution(unittest.TestCase):
   def test_validate_binary_search_tree(self):
        solution = Solution()

        #     2
        #    / \
        #   1   3
        tree = TreeNode(2)
        tree.left = TreeNode(1)
        tree.right = TreeNode(3)
        self.assertTrue(solution.isValidBST(tree))

        #     5
        #    / \
        #   1   4
        #      / \
        #     3   6
        tree = TreeNode(5)
        tree.left = TreeNode(1)
        tree.right = TreeNode(4)
        tree.right.left = TreeNode(3)
        tree.right.right = TreeNode(6)
        self.assertFalse(solution.isValidBST(tree))

        #     0
        #      \
        #       -1
        tree = TreeNode(0)
        tree.right = TreeNode(-1)
        self.assertFalse(solution.isValidBST(tree))

        #     0
        #    /
        #  -1
        tree = TreeNode(0)
        tree.left = TreeNode(-1)
        self.assertTrue(solution.isValidBST(tree))

if __name__ == '__main__':
    unittest.main()