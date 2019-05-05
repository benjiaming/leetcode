import unittest
from find_duplicate_subtrees import Solution, TreeNode

class TestSolution(unittest.TestCase):
    def test_find_duplicate_subtrees(self):
        solution = Solution()

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(4)
        root.right = TreeNode(3)
        root.right.left = TreeNode(2)
        root.right.left.left = TreeNode(4)
        root.right.right = TreeNode(4)
        self.assertEqual(str(solution.findDuplicateSubtrees(root)), str([4,2]))

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(5)
        self.assertEqual(solution.findDuplicateSubtrees(root), [])

if __name__ == '__main__':
    unittest.main()