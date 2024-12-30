# 바이러스 BFS
from collections import deque

n = int(input()) # 컴퓨터의 수
v = int(input()) # 연결 선 개수

graph = [[] for i in range(n+1)] # 그래프 초기화
visited = [0] * (n+1) # 방문 처리

for i in range(v): # 그래프 생성
    a, b = map(int, input().split())
    # 양방향 연결 (a <-> b)
    graph[a] += [b]
    graph[b] += [a]

visited[1] = 1 # 1번 컴퓨터부터 시작이므로, 방문 표시

Q = deque(1)
while Q:
    c = Q.popleft()
    for nx in graph[c]:
        if visited[nx] == 0:
            Q.append(nx)
            visited[nx] = 1

# 1번 컴퓨터를 감염된 컴퓨터의 수로 측정해서, 전체에서 1을 빼줘야 감염된 컴퓨터의 수를 출력            
print(sum(visited)-1)