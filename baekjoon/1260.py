from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())

Graph = [[False] * (n+1) for _ in range(n+1)]

for i in range(m):
    num1, num2 = map(int, input().split())
    Graph[num1][num2] = True
    Graph[num2][num1] = True

# 방문 기록 초기화
visited1 = [False] * (n+1)
visited2 = [False] * (n+1)

def dfs(v):
    # 방문처리
    visited1[v] = True
    # 처리 후 정점 출력
    print(v, end=' ')
    for i in range(1, n+1):
        # 방문 기록이 없고, 연결되어 있으면
        if not visited1[i] and Graph[v][i]:
            dfs(i)

def bfs(v):
    # 방문할 곳을 순서대로 넣을 큐
    q = deque([v])
    # 방문 처리
    visited2[v] = True
    
    while q:
        # 큐의 맨 앞에 있는 값을 꺼내서 출력
        v = q.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            # 방문 기록이 없고, 연결되어 있으면
            if not visited2[i] and Graph[v][i]:
                q.append(i)
                visited2[i] = True
dfs(v)
print()
bfs(v)



