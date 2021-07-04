"""
Use a dimension to sort.
Use other dimension to find out if there is someone before this person who satisfies the conditions.
"""
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        HW = []
        for i in range(n):
            h, w = map(int, input().split())
            HW.append((h, w, i))
            HW.append((w, h, i))  # This considers when the person is laying down
        # Sorting by first term, while ties we second in reverse using second term
        HW.sort(key=lambda x: (x[0], -x[1]))

        Answers = [-2 for i in range(n)]  # In result we add 1 so, -2 + 1 => -1 if no answer

        MinSecondDimension = float("inf")
        MinIndex = -2

        # print(HW)

        for i in range(2 * n):
            x, y, idx = HW[i]

            if y > MinSecondDimension:
                Answers[idx] = MinIndex
            else:
                MinSecondDimension = y
                MinIndex = idx

        for i in range(n):
            print(Answers[i] + 1, end=" ")
        print()
