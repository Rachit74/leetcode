#include <iostream>
#include <string>
#include <unordered_map>

bool isAnagram(std::string s, std::string t) {
    // check length
    if (s.length() != t.length()) {
        return false;
    }

    std::unordered_map<char, int> count;

    // increase count value by one for each character
    for (char c: s) {
        count[c]++;
    }

    for (char c: t) {
        count[c]--;
        if (count[c] < 0) {
            return false;
        }
    }
    
    return true;

}

// we can also build two maps and compare them
bool isAnagram2(std::string s, std::string t) {
    std::unordered_map<char, int> countS, countT;

    for (char c : s) countS[c]++;
    for (char c : t) countT[c]++;

    return countS == countT;
}