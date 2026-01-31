"""
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

    Every open bracket is closed by the same type of close bracket.
    Open brackets are closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Return true if s is a valid string, and false otherwise.
"""

"""
"""

def isValid(s: str):
    stack = []

    map_ = { ")" : "(", "]" : "[", "}" : "{" }

    for c in s:
        if c in map_:
            if stack and stack[-1] == map_[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)

    return True if not stack else False


test_cases = ["[]", "()"]

for case in test_cases:
    print(isValid(case))