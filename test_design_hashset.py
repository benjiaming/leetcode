import unittest
from design_hashset import MyHashSet

class TestSolution(unittest.TestCase):
    def test_design_hashset(self):
        obj = MyHashSet()
        self.assertFalse(obj.contains(1))
        obj.add(1)
        self.assertTrue(obj.contains(1))
        obj.add(2)
        self.assertTrue(obj.contains(2))
        self.assertFalse(obj.contains(3))
        obj.add(2)
        self.assertTrue(obj.contains(2))
        obj.remove(2)
        self.assertFalse(obj.contains(2))
 
if __name__ == '__main__':
    unittest.main()