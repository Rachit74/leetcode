"""
Given two strings s and t, return true if t is an

of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

https://leetcode.com/problems/valid-anagram/description/

"""

def validAnagram(s,t):

    #return sorted(s) == sorted(t)
    # return Counter(s) == Counter(t)

    # return flase if lengths don't match
    if len(s) != len(t):
        return False
    
    count = {}

    for char in s:
        count[char] = count.get(char, 0) + 1


    for char in t:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1

    return True

s1 = "rachit"
s2 = "mudit"
s3 = "rachit"

print(validAnagram(s1,s2))
print(validAnagram(s1,s1))
