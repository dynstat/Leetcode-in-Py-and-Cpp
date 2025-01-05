from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:
    # Using the two pointers approach
    l = 0
    r = len(numbers) - 1

    while l < r:
        added = numbers[l] + numbers[r]
        if added == target:
            return [l + 1, r + 1]
        elif added > target:
            r -= 1
        elif added < target:
            l += 1


print(twoSum([2, 7, 11, 15], 9))
