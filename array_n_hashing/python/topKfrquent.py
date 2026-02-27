
nums = [1,1,1,2,2,3]
k = 2

def topKfrequent(nums, k):
    result = list()

    map = {}

    for num in nums:
        map[num] = map.get(num, 0) + 1

    result = sorted(map, key=map.get, reverse=True)
    print(result[:k])

topKfrequent(nums, k)