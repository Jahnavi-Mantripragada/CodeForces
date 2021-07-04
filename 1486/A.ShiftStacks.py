from collections import Counter
def Possible(n, h):
    if len(set(h)) == n and sorted(h) == h:
        return True


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        h = list(map(int, input().split()))
        if Possible(n, h):
            print("YES")
        else:
            print("NO")