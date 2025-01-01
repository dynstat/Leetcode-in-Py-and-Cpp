from collections import defaultdict


def countGoodSubstrings(s: str) -> int:
    map = defaultdict(int)
    slen = len(s)
    ans = 1
    l = 0
    r = 2
    if slen < 3:
        return 0
    for i in range(3):
        if s[i] in map:
            ans = 0
        map[s[i]] += 1

    while r < slen:
        l += 1
        r += 1
        if r >= slen:
            return ans
        # check if good substring or not
        if len(set(s[l : r + 1])) == 3:
            ans += 1
    return ans


if __name__ == "__main__":
    print(countGoodSubstrings("xyzzaz"))
    print(countGoodSubstrings("aababcabc"))
