# -*- coding: utf-8 -*-
"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!

Example :

Input: n = 10, pick = 6
Output: 6

"""
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0

#%%
from random import randint
my_num = randint(1, 10)
def guess(num):
    if my_num < num:
        return -1
    elif my_num > num: 
        return 1
    return 0

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n
        while left <= right:
            middle = left + (right - left) // 2
            my_guess = guess(middle)
            if my_guess == 0:
                return middle
            if my_guess == -1:
                right = middle - 1
            else:
                left = middle + 1
        return -1
 
solution = Solution()
print(solution.guessNumber(10))

#%%
