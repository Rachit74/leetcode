"""
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
"""

"""
we first convert the string chars to lower case (or any one single case)
we make two pointers, one at the start of the string and another at the end 
we compare the char at both the pointers, if they are not same we return False
if they are same, we move to the next chars by incrementing the first pointer and decrementing the second pointer
"""

def isPalindrome(s: str) -> bool:
    # conver the string to lower case
    s = s.lower()

    # pointers to the start and end of the list
    p1 = 0
    p2 = len(s) - 1

    while p1 < p2:
        if not s[p1].isalnum():
            p1 += 1
            continue
        elif not s[p2].isalnum():
            p2 -= 1
            continue

        if s[p1] != s[p2]:
            return False
        
        p1 += 1
        p2 -= 1

    return True


test_cases = [
    "lol",
    "Was it a car or a cat I saw?",
    "tab a cat",
]

for case in test_cases:
    print(isPalindrome(case))
