import string

alpha = string.ascii_lowercase


def IsaAlphabeticalString(S):
    if "".join(sorted(S)) != alpha[:len(S)]:
        return False
    pos = dict()
    for i in range(len(S)):
        if S[i] in pos:
            return False
        pos[S[i]] = i
    prev = None
    count = 0
    left_end = 0
    right_end = 0
    for x in sorted(pos):
        count += 1
        if prev is None:
            prev = pos[x]
            left_end = pos[x]
            right_end = pos[x]
            continue
        if abs(prev - pos[x]) != 1 and abs(prev - pos[x]) != count - 1:
            # print(x, pos[x], prev, count)
            return False
        if pos[x] != left_end - 1 and pos[x] != right_end + 1:
            return False
        left_end = min(left_end, pos[x])
        right_end = max(right_end, pos[x])
        prev = pos[x]
    return True


if __name__ == "__main__":
    t = int(input())
    for case in range(t):
        S = input()
        if IsaAlphabeticalString(S):
            print("YES")
        else:
            print("NO")
