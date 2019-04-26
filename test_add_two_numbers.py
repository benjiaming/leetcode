import unittest
from add_two_numbers import Solution, ListNode

class TestSolution(unittest.TestCase):
    def test_add_two_numbers(self):
        solution = Solution()
        ln1 = ListNode(2)
        ln1.next = ListNode(4)
        ln1.next.next = ListNode(3)
        ln2 = ListNode(5)
        ln2.next = ListNode(6)
        ln2.next.next = ListNode(4)
        ln3 = ListNode(7)
        ln3.next = ListNode(0)
        ln3.next.next = ListNode(8)
        added = solution.addTwoNumbers(ln1, ln2)
        self.assertEqual(int(added.val), 7)
        self.assertEqual(int(added.next.val), 0)
        self.assertEqual(int(added.next.next.val), 8)


if __name__ == '__main__':
    unittest.main()