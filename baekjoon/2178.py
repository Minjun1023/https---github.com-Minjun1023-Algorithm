from collections import deque

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

def bfs(x, y):
    # 상 하 좌 우 방향 정의
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        # 4가지 방향 위치 확인(상,하,좌,우)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 지정
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            # 0인 경우 벽으로 지정
            if graph[nx][ny] == 0:
                continue
            # 1인 경우
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 탈출
    return graph[N-1][M-1]
# 출력
print(bfs(0,0))
