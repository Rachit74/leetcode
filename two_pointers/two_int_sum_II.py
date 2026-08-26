# problem link: https://neetcode.io/problems/two-integer-sum-ii/question?list=neetcode150

def twoSum(numbers, target) -> list[int]:
    p1 = 0
    p2 = len(numbers) - 1

    while p1 < p2:
        current_sum = numbers[p1] + numbers[p2]

        if current_sum > target:
            p2 -= 1
        elif current_sum < target:
            p1 += 1
        else:
            return [p1 + 1, p2 + 1]

numbers = [1,2,3,4]
target = 3

print(twoSum(numbers, target))