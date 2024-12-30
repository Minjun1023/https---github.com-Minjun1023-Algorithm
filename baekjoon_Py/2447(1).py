# 풀이1: 별을 9개의 공간으로 나눈 뒤 중앙값을 제외한 나머지 공간에 별을 복사
import sys
sys.setrecursionlimit(10**6) # 재귀 깊이 지정
input = sys.stdin.readline

def paint_star(LEN):
    DIV3 = LEN // 3
    if LEN == 3: # 3의 패턴
        g[1] = ['*', ' ', '*']
        g[0][:3] = g[2][:3] = ['*'] * 3
        return
    
    paint_star(DIV3) 

    for i in range(0, LEN, DIV3): # 행 시작점
        for j in range(0, LEN, DIV3): # 열 시작점
            if i != DIV3 or j != DIV3: # 중앙값이 아닌 경우
                for k in range(DIV3): # 3 패턴 복사
                    g[i+k][j:j+DIV3] = g[k][:DIV3]

n = int(input().strip())
g = [[' ' for _ in range(n)] for _ in range(n)]

paint_star(n)

for i in range(n):
    for j in range(n):
        print(g[i][j], end='')
    print() 


