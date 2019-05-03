import unittest
from minimum_index_sum_of_two_lists import Solution

class TestSolution(unittest.TestCase):
    def test_minimum_index_sum_of_two_lists(self):
        solution = Solution()
        self.assertEqual(solution.findRestaurant(['a', 'b', 'c'], ['b', 'c', 'a']), ['b'])
        self.assertEqual(solution.findRestaurant(
            ["Shogun", "Tapioca Express", "Burger King", "KFC"],
            ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
        ), ['Shogun'])
        self.assertEqual(solution.findRestaurant(
            ["Shogun", "Tapioca Express", "Burger King", "KFC"], 
            ["KFC", "Shogun", "Burger King"]
        ), ['Shogun'])

if __name__ == '__main__':
    unittest.main()