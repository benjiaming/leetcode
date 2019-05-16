"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

"""
#%%
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        Time complexity: O(N). Space complexity: O(1)
        """
    
        if len(prices) < 2:
            return 0
        
        min_price = prices[0]
        best_price = prices[1] - prices[0]
        for i, n in enumerate(prices, 1):
            min_price = min(prices[i-1], min_price)
            diff_curr_min = n - min_price
            best_price = max(best_price, diff_curr_min)
        if best_price < 0:
            return 0
        return best_price

solution = Solution()
print(solution.maxProfit([4,5,1,7,2,8]))
print(solution.maxProfit([7,6,5,4,3]))
print(solution.maxProfit([7,1,5,3,6,4]))
print(solution.maxProfit([1,2,4]))

#%%
