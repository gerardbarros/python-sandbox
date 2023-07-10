"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false


Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.


Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""

# two strings, s & t. If t is anagram of s, return True, if not return False
# s = art, t = tar => true
# s = bar, t = bat => false

def checkAnagram(s, t):
    # check if length is same
    if len(s) != len(t):
        return False
    
    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0) #character s at index i [s[i]], increment the count by 1. gets key, 0 is default value
        countT[t[i]] = 1 + countT.get(t[i], 0)
    # iterate through HM and make sure count is same
    return countS == countT

print(checkAnagram("art", "tar"))
print(checkAnagram("bar", "bat"))
