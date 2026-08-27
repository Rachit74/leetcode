# problem link: https://neetcode.io/problems/three-integer-sum/question?list=neetcode150

def threeSum(nums):
    nums.sort()
    return_list = []


    for i in range(len(nums) - 2):
        #skip dublicate elements
        if i > 0 and nums[i] == nums[i-1]:
            continue

        p1 = i + 1
        p2 = len(nums) - 1

        while p1 < p2:
            current_sum = nums[p1] + nums[p2]
            target = -nums[i]

            if current_sum < target:
                p1 += 1
            elif current_sum > target:
                p2 -= 1
            else:
                return_list.append([nums[i], nums[p1], nums[p2]])
                while p1 < p2 and nums[p1] == nums[p1 + 1]:
                    p1 += 1
                while p1 < p2 and nums[p2] == nums[p2 - 1]:
                    p2 -= 1
                
                p1 += 1
                p2 -= 1

    return return_list


nums = [-1,0,1,2,-1,-4]

print(threeSum(nums))