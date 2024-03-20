# 74. Search a 2D Matrix
# Solved
# Medium
# Topics
# Companies
# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.


# Example 1:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Example 2:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false


# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    # matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    # target = 3
    m2 = [num for sublist in matrix for num in sublist]
    l = len(m2)
    left = 0
    right = l - 1

    while left <= right:
        mid = left + (right - left) // 2
        mid_val = m2[mid]
        if mid_val == target:
            return True
        elif mid_val < target:
            left = mid + 1
        elif mid_val > target:
            right = mid - 1
    return False


if __name__ == "__main__":
    print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
