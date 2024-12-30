# 배열에 자연수 x를 넣는다.
# 배열에서 가장 큰 값을 출력, 그 값을 배열에서 제거
import sys
import heapq
input = sys.stdin.readline

N = int(input())
q = []
for i in range(N):
  x = int(input())
  if x == 0:
    if len(q) == 0:
      print(0)
    else:
      print(-heapq.heappop(q))
  else:
    heapq.heappush(q,-x)


