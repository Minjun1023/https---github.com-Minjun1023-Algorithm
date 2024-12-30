# 바이러스 DFS

n = int(input()) # 컴퓨터의 수
v = int(input()) # 연결선 수

graph = [[] for i in range(n+1)] # 그래프 초기화
visited = [0] * (n+1) # 방문 처리

for i in range(v): # 그래프 생성
    a, b = map(int, input().split())
    # 양방향 연결 (a <-> b)
    graph[a] += [b]
    graph[b] += [a]

def dfs(v):
    visited[v] = 1
    for nx in graph[v]:
        if visited[nx] == 0:
            dfs(nx)

dfs(1)
print(sum(visited) - 1)
