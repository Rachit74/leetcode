#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>
#include <array>

std::vector<std::vector<std::string>> groupAnagrams(std::vector<std::string> &strs) {
    std::unordered_map<std::string, std::vector<std::string>> groups;

    for (std::string s : strs) {
        std::array<int, 26> count = {0};
        for (char c : s) {
            count[c - 'a']++;
        }

        std::string key = "";
        for (int i = 0; i < 26; i++) {
            key += std::to_string(count[i])+ "#";
        }

        groups[key].push_back(s);
        
    }

    std::vector<std::vector<std::string>> result;
    for (auto& pair : groups) {
        result.push_back(pair.second);
    }
    return result;


}