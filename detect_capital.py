"""
 Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

    All letters in this word are capitals, like "USA".
    All letters in this word are not capitals, like "leetcode".
    Only the first letter in this word is capital if it has more than one letter, like "Google".

Otherwise, we define that this word doesn't use capitals in a right way.

Example 1:

Input: "USA"
Output: True

Example 2:

Input: "FlaG"
Output: False

Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters. 
"""
#%%

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        first_is_capital = word[0].isupper()
        second_is_capital = word[1].isupper()
        if not first_is_capital and second_is_capital:
            return False
        must_be_lowercase = True
        if first_is_capital and second_is_capital:
            must_be_lowercase = False
        for i in range(2, len(word)):
            if word[i].isupper():
                if must_be_lowercase:
                    return False
            else:
                if not must_be_lowercase:
                    return False
        return True
        
solution = Solution()
print(solution.detectCapitalUse('FlaG')) # False
print(solution.detectCapitalUse('Flag')) # True
print(solution.detectCapitalUse('flaG')) # False
print(solution.detectCapitalUse('USA')) # True
print(solution.detectCapitalUse('US')) # True
print(solution.detectCapitalUse('uS')) # False
print(solution.detectCapitalUse('cVe')) # False



#%%
