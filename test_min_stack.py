import unittest

from list_node import ListNode
from min_stack import MinStack

class TestSolution(unittest.TestCase):
   def test_min_stack(self):
        minStack = MinStack()
        self.assertEqual(minStack.top(), None)
        self.assertEqual(minStack.getMin(), None)
        self.assertEqual(minStack.stack, [])
        minStack.push(-2)
        self.assertEqual(minStack.top(), -2)
        self.assertEqual(minStack.getMin(), -2)
        self.assertEqual(minStack.stack, [-2])
        minStack.push(0)
        self.assertEqual(minStack.top(), 0)
        self.assertEqual(minStack.getMin(), -2)
        self.assertEqual(minStack.stack, [-2, 0])
        minStack.push(-3)
        self.assertEqual(minStack.top(), -3)
        self.assertEqual(minStack.getMin(), -3)
        self.assertEqual(minStack.stack, [-2, 0, -3])
        minStack.push(3)
        self.assertEqual(minStack.top(), 3)
        self.assertEqual(minStack.getMin(), -3)
        self.assertEqual(minStack.stack, [-2, 0, -3, 3])
        minStack.pop()
        self.assertEqual(minStack.top(), -3)
        self.assertEqual(minStack.getMin(), -3)
        self.assertEqual(minStack.stack, [-2, 0, -3])

        minStack = MinStack()
        minStack.push(-2)
        minStack.push(0)
        minStack.push(-3)
        self.assertEqual(minStack.getMin(), -3)
        self.assertEqual(minStack.min_stack, [-2, -3])
        minStack.pop()
        self.assertEqual(minStack.top(), 0)
        self.assertEqual(minStack.min_stack, [-2])
        self.assertEqual(minStack.getMin(), -2)

        minStack = MinStack()
        minStack.push(0)
        self.assertEqual(minStack.min_stack, [0])
        minStack.push(1)
        self.assertEqual(minStack.min_stack, [0])
        minStack.push(0)
        self.assertEqual(minStack.getMin(), 0)
        self.assertEqual(minStack.min_stack, [0,0])
        minStack.pop()
        self.assertEqual(minStack.min_stack, [0])
        self.assertEqual(minStack.getMin(), 0)
    

if __name__ == '__main__':
    unittest.main()