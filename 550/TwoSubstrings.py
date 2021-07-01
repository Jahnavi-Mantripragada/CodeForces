"""
https://codeforces.com/problemset/problem/550/A
"""
"""
0 1 2 3
A B A B
"""


def twoSubstrings(s):
    if "AB" not in s or "BA" not in s:
        return "NO"
    found_ab = -1
    for i in range(1, len(s)):
        if s[i-1] + s[i] == "AB":
            found_ab = i-1
            break

    for i in range(found_ab+2, len(s)-1):
        if s[i] + s[i+1] == "BA":
            return "YES"
    found_ba = -1
    for i in range(1, len(s)):
        if s[i - 1] + s[i] == "BA":
            found_ba = i - 1
            break
    for i in range(found_ba + 2, len(s)-1):
        if s[i] + s[i+1] == "AB":
            return "YES"
    return "NO"


if __name__ == "__main__":
    print(twoSubstrings(input()))
