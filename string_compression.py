"""
Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.
 

Follow up:
Could you solve it using only O(1) extra space?
 

Example 1:

Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
"""
#%%
from collections import Counter

class Solution(object):
    def compress(self, chars):
        i, j, index, count = 0, 0, 0, 0
        chlen = len(chars)
        while i < chlen:
            while i < chlen and chars[i] == chars[index]:
                count += 1
                i += 1
            chars[j] = chars[index]
            j += 1
            index = i
            if count != 1:
                temp = str(count)
                for t in temp:
                    chars[j] = t
                    j += 1
            count = 0
        return j    

    def compress2(self, chars):
        """
        Modification from CrackingTheCodingInterview.com

        aabbccccaa => a2b1c5a3
        """

        if len(chars) < 2:
            return chars
        output = ''
        prev_char = chars[0]
        prev_char_count = 1
        for i in range(1, len(chars)):
            if chars[i] == prev_char:
                prev_char_count += 1
            else:
                output += prev_char
                output += str(prev_char_count)
                prev_char = chars[i]
                prev_char_count = 1
        output += prev_char
        output += str(prev_char_count)
        return output



solution = Solution()
input = ["a","a","b","b","c","c","c"]
print(solution.compress(input))
print(input)
input = ["a","b"]
print(solution.compress(input))
print(input)
input = ["a","b", "c"]
print(solution.compress(input))
print(input)
input = ["a","b", "c","d","e"]
print(solution.compress(input))
print(input)
input = ["a"]
print(solution.compress(input))

print(solution.compress2('aabbccc'))



#%%
