# 내리막 길
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for i in range(m)]
# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def is_range(x, y, now):
    # 범위 지정
    return 0 <= x < m and 0 <= y < n and graph[x][y] < now

def solution(x, y):
    # 도착 시 
    if x == m-1 and y == n-1:
        return 1
    # 방문 시
    if dp[x][y] == -1:
        dp[x][y] = 0
        # 상, 하, 좌, 우 방향
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if is_range(nx, ny, graph[x][y]):
                # 도착 시 경로의 개수 추가
                dp[x][y] += solution(nx, ny)
    
    return dp[x][y]

print(solution(0,0))

    

