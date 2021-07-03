# https://codeforces.com/problemset/problem/1328/B
import bisect


def k_th_beautiful_string(n, k):
    pos = bisect.bisect(starts, k) - 1
    START = starts[pos]
    diff = k - START
    # print(diff)
    start_string = ["b"] + ["a"] * pos + ["b"]
    index = -2
    for i in range(diff):
        start_string[index] = "b"
        start_string[index + 1] = "a"
        index -= 1
    return "".join(["a"] * (n - pos - 2) + start_string)


if __name__ == "__main__":
    t = int(input())
    starts = [1]
    for i in range(2, (10 ** 5) + 1):
        starts.append(i * (i - 1) // 2 + 1)

    for case in range(t):
        n, k = map(int, input().split())
        print(k_th_beautiful_string(n, k))
