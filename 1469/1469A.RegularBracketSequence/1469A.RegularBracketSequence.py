def Valid(s):
    return len(s) % 2 == 0 and s[0] != ')' and s[-1] != '('


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input().strip()
        if Valid(s):
            print("YES")
        else:
            print("NO")
