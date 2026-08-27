# problem link: https://neetcode.io/problems/max-water-container/question?list=neetcode150

def maxArea(heights):
    p1 = 0
    p2 = len(heights) - 1
    max_water = 0

    while p1 < p2:
        # area
        width = p2 - p1
        height = min(heights[p1], heights[p2])
        current_area = width * height

        max_water = max(max_water, current_area)

        if heights[p1] < heights[p2]:
            p1 += 1
        else:
            p2 -= 1

    return max_water


heights = [1,7,2,5,4,7,3,6]

print(maxArea(heights))