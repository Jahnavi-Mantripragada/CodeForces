def correctness(n, pc):
    prev = pc[0]
    if prev[0] < prev[-1]:
        return False
    for i in range(1, n):
        curr = pc[i]
        if curr[0] < curr[-1]:  # If # of plays < # of clears
            return False
        if prev[0] == curr[0]:  # Plays stay same but clears increase
            if prev[-1] != curr[-1]:
                return False
        if prev[0] > curr[0]:  # If number of plays decreases
            return False
        if prev[-1] > curr[-1]:  # If number of clears decreases
            return False
        if curr[0] - prev[0] < curr[-1] - prev[-1]:  # If the diff(plays) < diff(clears)
            return False
        prev = pc[i]
    return True


if __name__ == "__main__":
    T = int(input())
    for case in range(T):
        n = int(input())
        pc = []
        for i in range(n):
            p, c = map(int, input().split())
            pc.append((p, c))
        if correctness(n, pc):
            print("YES")
        else:
            print("NO")
