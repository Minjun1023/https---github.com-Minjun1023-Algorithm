# 다익스트라
# 화폐의 단위 = 루피
# 검정 루피 = 소지한 루피가 감소
# 도둑 루피 가득한 N X N 크기의 동굴의 제일 왼쪽 위에 존재 [0][0]
# 출구 = 제일 오른쪽 칸: [N-1][N-1]
# 동굴의 칸마다 도둑 루피 존재
# 이 칸을 지나면 해당 도둑루피의 크기만큼 소지금을 잃게 됨
# 링크는 잃는 금액을 최소로 하여 동굴 건너편까지 이동해야함. 한 번에 상하좌우 인접한 곳으로 1칸 이동 가능
# 출력: 잃을 수 밖에 없는 최소 금액
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 1

def dijkstra():
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    distance[0][0] = 0

    while q:
        cost, x, y = heapq.heappop(q)

        if x == n - 1 and y == n-1:
            print(f'Problem {count}: {distance[x][y]}')
            break
        
        # 상,하,좌,우 방향
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 방향
            if 0 <= nx < n and 0 <= ny < n:
                new_cost = cost + graph[nx][ny]
                # distance에 있는 값과 비교
                if new_cost < distance[nx][ny]:
                    distance[nx][ny] = new_cost
                    heapq.heappush(q, (new_cost, nx, ny))

while True:
    n = int(input())
    if n == 0:
        break    

    graph = [list(map(int, input().split())) for _ in range(n)]
    distance = [[INF] * n for _ in range(n)]

    dijkstra()
    count += 1




