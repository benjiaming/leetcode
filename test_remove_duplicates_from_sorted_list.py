import unittest
from remove_duplicates_from_sorted_list import Solution, ListNode

class TestSolution(unittest.TestCase):
    def test_remove_duplicates_from_sorted_list(self):
        # 1->1->2 => 1->2
        head = ListNode(1)
        head.next = ListNode(1)
        head.next.next = ListNode(2)
        before = ListNode.traverse(head)
        self.assertEqual(before, '1->1->2')

        solution = Solution()
        solution.deleteDuplicates(head)
        after = ListNode.traverse(head)
        self.assertEqual(after, '1->2')

        # 1->1->2->3->3 => 1->2->3
        head = ListNode(1)
        head.next = ListNode(1)
        head.next.next = ListNode(2)
        head.next.next.next = ListNode(3)
        head.next.next.next.next = ListNode(3)
        before = ListNode.traverse(head)
        self.assertEqual(before, '1->1->2->3->3')

        solution.deleteDuplicates(head)
        after = ListNode.traverse(head)
        self.assertEqual(after, '1->2->3')

        # 1->1->1->1 => 1
        head = ListNode(1)
        head.next = ListNode(1)
        head.next.next = ListNode(1)
        head.next.next.next = ListNode(1)
        head.next.next.next.next = ListNode(1)
        before = ListNode.traverse(head)
        self.assertEqual(before, '1->1->1->1->1')

        solution.deleteDuplicates(head)
        after = ListNode.traverse(head)
        self.assertEqual(after, '1')


if __name__ == '__main__':
    unittest.main()