#https://codeforces.com/problemset/problem/1369/B
def accurateLee(n,s):
  if n == 0 or n == 1:
    return s
  one_starts = -1
  for i in range(n):
    if s[i] == '1':
      one_starts = i
      break
  # print("ONE STARTS: ", one_starts)
  zero_ends = -1
  index = n-1
  while index > one_starts:
    if s[index] == '0':
      zero_ends = index
      break
    index-=1
  # print("ZERO ENDS: ", zero_ends)
  if one_starts == -1 or zero_ends == -1:
    return s
  
  return s[:one_starts] + s[zero_ends:]
  


if __name__ == "__main__":
  t = int(input())
  for case in range(t):
    n = int(input())
    s = input()
    print(accurateLee(n,s))