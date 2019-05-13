import unittest
from design_hashmap import MyHashMap

class TestSolution(unittest.TestCase):
    def test_design_hashmap(self):
        hashmap = MyHashMap()
        hashmap.put(1, 1)
        hashmap.put(2, 2)
        self.assertEqual(hashmap.get(1), 1)
        self.assertEqual(hashmap.get(3), -1) # not found
        hashmap.put(2, 1)
        self.assertEqual(hashmap.get(2), 1) # update the existing value
        hashmap.remove(2)
        self.assertEqual(hashmap.get(2), -1)

if __name__ == '__main__':
    unittest.main()