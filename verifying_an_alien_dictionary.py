# -*- coding: utf-8 -*-
"""
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).

 

Note:

    1 <= words.length <= 100
    1 <= words[i].length <= 20
    order.length == 26
    All characters in words[i] and order are english lowercase letters.
"""
#%%
class Solution(object):
    def isListSorted(self, nums):
        if len(nums) < 2:
            return True
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                return False
        return True

    def listHasDups(self, nums):
        if len(nums) <= 1:
            return False
        for j in range(1, len(nums)):
            if nums[j] == nums[j-1]:
                return True
        return False

    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        if len(words) < 2:
            return True
        order_dict = {o:i for i, o in enumerate(order)}
        matrix = []
        for w in words:
            line = []
            for o in w:
                line.append(order_dict[o])
            matrix.append(line)

        print (matrix)
        prev_row = ()
        for row in zip(*matrix):
            print(row)
            if self.isListSorted(row):
                if len(row) >= len(prev_row) and row != prev_row and not self.listHasDups(row):
                    return True
            else:
                return False
            prev_row = row
        prev_len = len(words[0])
        for w in range(1, len(words)):
            if len(words[w]) < prev_len:
                return False
        return True


solution = Solution()
print(solution.isAlienSorted(words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"))
print(solution.isAlienSorted(words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"))
print(solution.isAlienSorted(words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"))

# print(solution.isListSorted([4,5,6,6]))
# print(solution.isListSorted([6,5,4,10]))


#%%
