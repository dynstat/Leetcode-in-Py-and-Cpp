# OPTIMIZED SLIDING WINDOW
def countKConstraintSubstrings(self, s: str, k: int) -> int:
    left = 0
    zeros, ones = 0, 0
    count = 0

    for right in range(len(s)):
        # Expand the window
        if s[right] == "0":
            zeros += 1
        else:
            ones += 1

        # Shrink the window if constraints are violated
        while zeros > k and ones > k:
            if s[left] == "0":
                zeros -= 1
            else:
                ones -= 1
            left += 1

        # Add the number of valid substrings ending at 'right'
        count += right - left + 1

    return count


# 2 POINTERS method Sliding Window
def countKConstraintSubstrings_sliding(self, s: str, k: int) -> int:
    n = len(s)
    count = 0

    # For each starting point
    for left in range(n):
        zeros = 0
        ones = 0

        # Expand window until either count exceeds k
        for right in range(left, n):
            if s[right] == "0":
                zeros += 1
            else:
                ones += 1

            # If either count is <= k, it's a valid substring
            if zeros <= k or ones <= k:
                count += 1
            # If both counts exceed k, break inner loop
            elif zeros > k and ones > k:
                break

    return count


# BRUTE FORCE APPROACH
def countKConstraintSubstrings_bf(self, s: str, k: int) -> int:
    s_len = len(s)
    ans = 0
    for start in range(s_len):
        for end in range(start, s_len):
            substr = s[start : end + 1]
            # conditions -> no. of 0s == k || no. of 1s == k
            sub_idx = 0
            count_0 = 0
            count_1 = 0
            while sub_idx < len(substr):
                if substr[sub_idx] == "0":
                    count_0 += 1
                else:
                    count_1 += 1
                sub_idx += 1
            # print(f"substr = {substr}, count_0 = {count_0}, count_1 = {count_1}")
            if not (count_0 > k and count_1 > k):
                ans += 1
            # else:
            #     break
    return ans


if __name__ == "__main__":
    print(countKConstraintSubstrings("000011", 1))
    print(countKConstraintSubstrings("1010101", 2))
