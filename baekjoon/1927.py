# 최소 힙
# 배열에 자연수 x를 넣는다.
# 배열에서 가장 작은 값을 출력, 그 값을 배열에서 제거

import sys
import heapq # 최소 힙을 얻기 위해 사용함
input = sys.stdin.readline

N = int(input())
q = []
for i in range(N):
  x = int(input())
  if x == 0: # 만약 배열이 비어있는 경우. 가장 작은 값을 출력할 경우 0 출력
    if len(q) == 0:
      print(0)
    else: # 아닐 경우 heappop 사용해서 가장 작은 값 출력하고 그 값을 배열에서 제거함
      print(heapq.heappop(q))
  else: # 그 외의 경우 x를 q에 추가
    heapq.heappush(q, x)    