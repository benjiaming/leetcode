import unittest
from maximum_depth_of_binary_tree import Solution, TreeNode

class TestSolution(unittest.TestCase):
    def test_maximum_depth_of_binary_tree(self):
        solution = Solution()
        tree = TreeNode(3)
        tree.left = TreeNode(9)
        tree.right = TreeNode(20)
        tree.right.left = TreeNode(15)
        tree.right.right = TreeNode(7)

        self.assertEqual(solution.maxDepth(tree), 3)


if __name__ == '__main__':
    unittest.main()