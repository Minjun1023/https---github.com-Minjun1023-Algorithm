import sys
input = sys.stdin.readline

a = input().split('-')
lst = []

for i in a:
  sum = 0
  tmp = i.split('+')
  for j in tmp:
    sum += int(j)
  lst.append(sum)

n = lst[0]

for i in range(1, len(lst)):
  n -= lst[i]

print(n)