import unittest
from reverse_linked_list import Solution, ListNode

class TestSolution(unittest.TestCase):
    def test_reverse_linked_list(self):
        solution = Solution()
        node = ListNode(1)
        node.next = ListNode(2)
        node.next.next = ListNode(3)
        node.next.next.next = ListNode(4)
        node.next.next.next.next = ListNode(5)
        self.assertEqual(solution.traverse(node), '1->2->3->4->5')

        new_node = solution.reverseList(node)
        self.assertEqual(solution.traverse(new_node), '5->4->3->2->1')



if __name__ == '__main__':
    unittest.main()