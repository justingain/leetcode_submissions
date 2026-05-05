# 1768. Merge Strings Alternately
# Approach: Two pointers
# Time: O(n) where n is the length of the longer string
# Space: O(n) for the result string
#
# Gotchas: 
# - Loop only up to min length, then handle leftovers separately
# - Use i: slice to grab remaining characters, not i alone

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        result = ""
        while i < min(len(word1), len(word2)):
            result += word1[i]+word2[i]
            i += 1
        if i < len(word1):
            result += word1[i:]
        elif i < len(word2):
            result += word2[i:]
        return result
print(Solution)
