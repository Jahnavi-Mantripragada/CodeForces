def InvertingDigit(t):
  return 9 - t 
def minPostiveNumber(x):
  d = list(map(int, x))
  if len(d) == 1:
    if d[0] == 9:
      return 9
    return min(InvertingDigit(d[0]), d[0])
  if d[0] != 9:
    d[0] = min(InvertingDigit(d[0]), d[0])
  for i in range(1, len(d)):
    d[i] = min(InvertingDigit(d[i]), d[i])
  return "".join(map(str,d))
if __name__ == "__main__":
  x = input()
  print(minPostiveNumber(x))