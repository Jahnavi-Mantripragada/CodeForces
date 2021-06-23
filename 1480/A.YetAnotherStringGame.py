def solve(string):
    new_string = []
    ATurn = True
    for x in string:
        if ATurn:
            if x == "a":
                new_string.append("b")
            else:
                new_string.append("a")
        else:
            if x == "z":
                new_string.append("y")
            else:
                new_string.append("z")
        ATurn = not ATurn
    return "".join(new_string)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        string = input()
        print(solve(string))
