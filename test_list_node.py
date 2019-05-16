import unittest
from list_node import ListNode

class TestSolution(unittest.TestCase):
    def test_list_node(self):
        node = ListNode([1,2,33,'a', 5,4,0])
        self.assertEqual(ListNode.traverse(node), '1->2->33->a->5->4->0')

        node = ListNode()
        self.assertEqual(ListNode.traverse(node), '')
        node.add('a')
        self.assertEqual(ListNode.traverse(node), 'a')
        node.add('b')
        self.assertEqual(ListNode.traverse(node), 'a->b')
        node.add('c')
        self.assertEqual(ListNode.traverse(node), 'a->b->c')
        node.add(0)
        self.assertEqual(ListNode.traverse(node), 'a->b->c->0')

if __name__ == '__main__':
    unittest.main()