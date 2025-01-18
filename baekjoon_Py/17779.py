# 1. 경계선 완전탐색
# 2. 인구가 가장 많은 선거구와 가장 적은 선거구의 인구 차이 값 구하기
# 3. 그 값의 최솟값 출력
import sys
input = sys.stdin.readline

n = int(input())
graph = [[]]
for _ in range(n):
    graph.append([0] + list(map(int, input().split())))

def man_count(x,y,d1,d2):
    # 5개의 선거구
    count = [0,0,0,0,0]
    # 경계구역 설정
    fifth = [[0 for _ in range(n+1)] for i in range(n+1)]
    for i in range(d1+1):
        fifth[x+i][y-i] = 1 # 왼쪽, 위로 향하는 대각선
        fifth[x+d2+i][y+d2-i] = 1 # 오른쪽, 위로 향하는 대각선
    for j in range(d2+1):
        fifth[x+j][y+j] = 1 # 오른쪽, 아래로 향하는 대각선
        fifth[x+d1+j][y-d1+j] = 1 # 왼쪽, 아래로 향하는 대각선
    for i in range(x+1, x+d1+d2):
        # flag = True : 경계선 내부, flag = False: 경계선 바깥
        flag = False # 경계선 안쪽 영역을 채우기 위한 상태
        for j in range(n+1): # 각 열을 탐색
            if fifth[i][j] == 1: # 경계선일 경우    
                if flag == True: 
                    flag = False 
                else:
                    flag = True
            else:
                if flag == True:
                    fifth[i][j] = 1
    for i in range(1,n+1):
        for j in range(1,n+1):
            # 1번, 2번, 3번, 4번 선거구의 범위
            if i < x+d1 and j <= y and fifth[i][j] != 1:
                count[0] += graph[i][j]
            elif i <= x+d2 and y < j and fifth[i][j] != 1:
                count[1] += graph[i][j]
            elif x+d1 <= i and j < y-d1+d2 and fifth[i][j] != 1:
                count[2] += graph[i][j]
            elif x+d2 < i and y-d1+d2 <= j and fifth[i][j] != 1:
                count[3] += graph[i][j]   
            elif fifth[i][j] == 1:
                count[4] += graph[i][j]
    return max(count) - min(count)
# 1번 선거구: 1 ≤ r < x+d1, 1 ≤ c ≤ y, 1번 경계선의 왼쪽 위
# 2번 선거구: 1 ≤ r ≤ x+d2, y < c ≤ N, 2번 경계선의 오른쪽 위
# 3번 선거구: x+d1 ≤ r ≤ N, 1 ≤ c < y-d1+d2, 3번 경계선의 왼쪽 아래
# 4번 선거구: x+d2 < r ≤ N, y-d1+d2 ≤ c ≤ N, 4번 경계선의 오른쪽 아래
# 5번 선거구: 그 외의 나머지 + 경계선
# 1. 경계선 완전탐색
min_count = float('inf')
for x in range(1, n+1):
    for y in range(1, n+1):
        for d1 in range(1, n+1):
            for d2 in range(1, n+1):
                if 1 <= x < x+d1+d2 <= n and 1 <= y-d1 < y < y+d2 <= n:
                    min_count = min(min_count, man_count(x,y,d1,d2))

print(min_count)