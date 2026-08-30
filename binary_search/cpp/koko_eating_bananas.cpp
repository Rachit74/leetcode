#include <vector>
#include <algorithm>
#include <iostream>

int minEatingSpeed(std::vector<int> &piles, int h) {
    std::sort(piles.begin(), piles.end());

    int maxPile = piles[piles.size() - 1];
    return maxPile;
}

int main() {
    std::vector<int> piles = {25,10,23,4};

    int sol = minEatingSpeed(piles, 4);

    std::cout << sol << "\n";
}