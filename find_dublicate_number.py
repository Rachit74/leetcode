"""
Docstring for find_dublicate_number

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2

Example 2:

Input: nums = [3,1,3,4,2]
Output: 3

https://leetcode.com/problems/find-the-duplicate-number/description/
"""
# using hash map
# we map each element as key and it's frquency as value, we reutrn the key which has a value more than 1.
def findDuplicate(nums):
        map = {}

        for n in nums:
            map[n] = map.get(n,0) + 1

        for v in map:
            if map[v] > 1:
                return v


# using sets
# we make two sets and return the first nums that is already present in seen
def findDuplicate(nums):
    seen = set()
    for n in nums:
            if n in seen:
                return n
            seen.add(n)

# using count array
# we map the count array to nums array using element of nums array as indexes to increase the value of elements of count array
def findDublicate(nums):
    count = [0] * (len(nums) + 1)

    for num in nums:
        count[num] += 1
        if count[num] > 1:
            return num


nums = [1,3,4,2,2]
print(findDublicate(nums))