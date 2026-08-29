#include <iostream>
#include <unordered_map>
#include <vector>

std::vector<int> twoSum(std::vector<int> &nums, int target) {
    std::unordered_map<int, int> map;

    int diff;

    for (int i = 0; i < nums.size(); i++) {
        map[nums[i]] = i;
    }

    for (int i = 0; i < nums.size(); i++) {
        diff = target - nums[i];
        if (map.find(diff) != map.end() && map[diff] != i) {
            return {i, map[diff]};
        }
    }

    return {};
}