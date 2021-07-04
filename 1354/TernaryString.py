def minSubstringLen(s):
    one, two, three = 0, 0, 0
    acquire = 0
    running_len = 0
    release = 0
    n = len(s)
    min_len = float("inf")
    while acquire < n:
        if s[acquire] == '1':
            one += 1
        elif s[acquire] == '2':
            two += 1
        elif s[acquire] == '3':
            three += 1
        acquire += 1
        running_len += 1
        while release < acquire and one > 0 and two > 0 and three > 0:
            min_len = min(min_len, running_len)
            if s[release] == '1':
                one -= 1
            elif s[release] == '2':
                two -= 1
            elif s[release] == '3':
                three -= 1
            running_len -= 1
            release += 1
    return min_len if min_len!=float("inf") else 0


if __name__ == "__main__":
    t = int(input())
    for case in range(t):
        s = input()
        print(minSubstringLen(s))
