# from functools import lru_cache
#
#
# @lru_cache(None)
# def FindDigits(length, sum_of_digits):
#     if length == 0:
#         return []
#     if not canMake(length, sum_of_digits):
#         return []
#     if length == 1:
#         if 0 <= sum_of_digits <= 9:
#             return [[sum_of_digits]]
#         else:
#             return []
#     if sum_of_digits < 0:
#         return []
#     Answer = set()
#     for i in range(min(10, sum_of_digits + 1)):
#         result = FindDigits(length - 1, sum_of_digits - i)
#         for x in result:
#             Answer.add(tuple(sorted([i] + list(x))))
#     return Answer

# Check if the sum is correct. (min: left most digit: 1, max: all nines)
def canMake(m, s):
    return 1 <= s <= m * 9


def GivenLengthAndSumOfDigits(m, s):
    # Case-1: s = 0
    if s == 0:
        if m == 1:
            return 0, 0
        else:
            return -1, -1
    # Case-2: m = 1
    if m == 1:
        if 1 <= s <= 9:
            return s, s
        else:
            return -1, -1
    if m == 0:
        return -1, -1
    if not(canMake(m, s)):
        return -1, -1

    # Maximum
    max_digit = 9
    number = [0]*m
    number[0] = 1
    dupe_s = s
    s -= 1
    i = m - 1
    while max_digit > 0 and i > 0:
        if s == 0:
            break
        if s >= max_digit:
            number[i] = max_digit
            s -= max_digit
            i -= 1
        else:
            max_digit -= 1
    if s > 0:
        number[0] += s
    minimum = int("".join(map(str, number)))
    s = dupe_s
    max_digit = 9
    number = [0]*m
    i = 0
    while max_digit > 0 and i < m:
        if s == 0:
            break
        if s >= max_digit:
            number[i] = max_digit
            i += 1
            s -= max_digit
        else:
            max_digit -= 1
    maximum = int("".join(map(str, number)))
    return minimum, maximum


if __name__ == "__main__":
    m, s = map(int, input().split())
    # d = list(FindDigits(7, 20))
    # d.sort()
    # for x in d:
#        print(x)
    d = GivenLengthAndSumOfDigits(m, s)
    print(d[0], d[1])
