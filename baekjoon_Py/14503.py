import sys
input = sys.stdin.readline

# 방향:  북 동 남 서 
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int ,input().split())) for _ in range(n)]

# 방문 처리
visited = [[0] * m for _ in range(n)]

# 처음 시작하는 곳 방문 처리
visited[r][c] = 1
cnt = 1

while 1:
    flag = 0
    # 4방향 확인
    for _ in range(4):
        nx = r + dx[(d+3)%4]
        ny = c + dy[(d+3)%4]
        # 한번 돌았으면 그 방향으로 작업 시작
        d = (d+3)%4
        # 범위 지정(n x m 크기의 방에서)
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
            # 청소되지 않은 칸일 경우
            if visited[nx][ny] == 0:
                # 한칸 전진하여 청소
                visited[nx][ny] = 1
                # 카운트 추가
                cnt += 1
                r, c = nx, ny
                # 청소 한 방향이라도 했으면 다음으로 넘어감
                flag = 1
                break
    if flag == 0: # 4방향 모두 청소 되어있을 경우
        if arr[r-dx[d]][c-dy[d]] == 1: # 후진하고나서 벽인 경우
            # 결과값 출력(청소하는 칸의 개수)
            print(cnt)
            break
        else: # 후진 가능
            r,c = r-dx[d], c-dy[d]







