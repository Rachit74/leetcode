#include <vector>

bool searchMatrix(std::vector<std::vector<int>> &matrix, int target) {
    if (matrix.empty()) return false;

    int rows = matrix.size();
    int cols = matrix[0].size();

    int left = 0;
    int right = rows * cols - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        // Convert 1D index to 2D coordinates
        int midValue = matrix[mid / cols][mid % cols];

        if (midValue == target) {
            return true;
        } else if (midValue < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }

    }
    return false;
}