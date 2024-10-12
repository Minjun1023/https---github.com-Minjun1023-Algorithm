from collections import deque

N = int(input())

# 입력값 저장
graph = []
for i in range(N):
    graph.append(list(map(int, input())))

# 상하좌우 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):

    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        # 4가지 방향
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            # 1인 경우 0으로 바꿔서 다시 방문 X
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count

cnt = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            cnt.append(bfs(i, j))

# 정렬
cnt.sort()

# 출력
print(len(cnt))

for i in range(len(cnt)):
    print(cnt[i])



    