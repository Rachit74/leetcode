#include <iostream>
#include <vector>
#include <unordered_set>

int longestConsecutive(std::vector<int> &nums) {
    std::unordered_set<int> num_set(nums.begin(), nums.end());
    int longest_streak = 0;

    for (int num : num_set) {
        // Check if this is the start of a sequence
        // start of the seq, if the number before it does not exist in the set
        if (num_set.find(num - 1) == num_set.end()) {
            int current_num = num;
            int current_streak = 1;
            
            // Count the length of the consecutive sequence
            while (num_set.find(current_num + 1) != num_set.end()) {
                current_num++;
                current_streak++;
            }
            
            longest_streak = std::max(longest_streak, current_streak);
        }
    }


    return longest_streak;
}