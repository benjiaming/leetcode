import unittest
from middle_of_linked_list import Solution
from list_node import ListNode

class TestSolution(unittest.TestCase):
   def test_middle_of_linked_list(self):
       solution = Solution()
       node = ListNode([1,2,3,4,5])
       self.assertEqual(solution.middleNode(node), 3)
       node = ListNode([1,2,3,4,5,6])
       self.assertEqual(solution.middleNode(node), 4)


if __name__ == '__main__':
    unittest.main()