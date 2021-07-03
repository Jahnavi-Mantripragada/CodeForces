"""
https://codeforces.com/problemset/problem/459/A
"""

if __name__ == "__main__":
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == x2:  # Line parallel to x-axis
        s = abs(y1 - y2)
        if x1 + s <= 1000:
            print(x1 + s, y1, x2 + s, y2)
        elif x1 - s >= -1000:
            print(x1 - s, y1, x2 - s, y2)
        else:
            print("-1")
    elif y1 == y2:  # Line parallel to y-axis
        s = abs(x1 - x2)
        if y1 + s <= 1000:
            print(x1, y1 + s, x2, y2 + s)
        elif y1 - s >= -1000:
            print(x1, y1 - s, x2, y2 - s)
        else:
            print("-1")
    else:
        if abs(x1 - x2) == abs(y1 - y2):  # Diagonals
            print(x2, y1, x1, y2)
        else:
            print("-1")
