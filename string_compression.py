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

# #%%


#%%
