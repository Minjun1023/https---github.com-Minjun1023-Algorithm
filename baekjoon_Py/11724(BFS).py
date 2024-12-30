# 방향 없는 그래프
from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True

  while queue:
    v = queue.popleft()
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

count = 0 # 연결 노드의 수
visited = [False] * (N+1) # 방문처리
for i in range(1, N+1):
  if not visited[i]:
    bfs(graph, i, visited) # bfs 한 번 끝날 때마다 count + 1
    count += 1

print(count)