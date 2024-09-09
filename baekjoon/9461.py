import sys
input = sys.stdin.readline

t = int(input())
arr = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9] # P(1)부터 P(10)까지의 숫자를 배열에 넣는다.

for i in range(11, 101): # n의 범위에 있는 값을 참고하여 11~100번까지 범위내에서 조합식을 계산해서 arr 배열에 넣는다.
  arr.append(arr[i-2] + arr[i-3])

for _ in range(t):
  n = int(input())
  # 출력
  print(arr[n])


