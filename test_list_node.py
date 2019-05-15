import unittest
from list_node import ListNode

class TestSolution(unittest.TestCase):
    def test_list_node(self):
        node = ListNode([1,2,33,'a', 5,4])
        self.assertEqual(ListNode.traverse(node), '1->2->33->a->5->4')

if __name__ == '__main__':
    unittest.main()