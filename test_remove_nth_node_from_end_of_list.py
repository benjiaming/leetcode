import unittest
from remove_nth_node_from_end_of_list import Solution
from list_node import ListNode

class TestSolution(unittest.TestCase):
    def test_remove_nth_node_from_end_of_list(self):
        solution = Solution()
        node = ListNode([1,2,3,4,5])
        before = '1->2->3->4->5'
        self.assertEqual(ListNode.traverse(node), before)
        solution.removeNthFromEnd(node, 2)
        after = '1->2->3->5'
        self.assertEqual(ListNode.traverse(node), after)

        node = ListNode([1])
        before = '1'
        self.assertEqual(ListNode.traverse(node), before)
        solution.removeNthFromEnd(node, 1)
        after = '1'
        self.assertEqual(ListNode.traverse(node), after)


if __name__ == '__main__':
    unittest.main()