import unittest
from insert_delete_get_random import RandomizedSet

class TestSolution(unittest.TestCase):
    def test_insert_delete_get_random(self):
        obj = RandomizedSet()
        self.assertTrue(obj.insert(1)) # [1]
        self.assertFalse(obj.remove(2)) # [1]
        self.assertTrue(obj.insert(2)) # [1,2]
        self.assertTrue(obj.getRandom() in [1,2])
        self.assertTrue(obj.remove(1)) # [2]
        self.assertFalse(obj.insert(2)) # [2]
        self.assertEqual(obj.getRandom(), 2) # [2]

if __name__ == '__main__':
    unittest.main()