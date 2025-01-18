# (row, col)의 행과 열은 d1,d2가 최소 1의 값을 가지므로, row는 0 ~ n-2 / col은 1 ~ n-1까지의 범위
import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
total = 0
for row in matrix:
    total += sum(row)
answer = int(1e9)

def calculate(row, col, d1, d2):
    global total, answer
    first, second, third, fourth = 0,0,0,0

    #구역 1
    col1 = col + 1
    for r in range(row+d1):
        if r >= row:
            col -= 1
        first += sum(matrix[r][:col1])
    
    #구역 2
    col2 = col + 1
    for r in range(row+d2+1):
        if r > row:
            col2 += 1
        second += sum(matrix[r][col2:])
    
    #구역 3
    col3 = col - d1
    for r in range(row+d1, n):
        third += sum(matrix[r][:col3])
        if r < row+d1+d2:
            col3 += 1
    
    #구역 4
    col4 = (col+d2) - n
    for r in range(row+d2+1, n):
        fourth += sum(matrix[r][col4:])
        if r <= row+d1+d2:
            col4 -= 1
    
    #구역 5
    five = total - first - second - third - fourth
    answer = min(answer, (max(first, second, third, fourth, five) - min(first, second, third, fourth, five)))

def check(r, c, d1, d2): # 가능한 d1, d2 찾기
    if 0 <= r+d1-1 < n and 0 <= r+d2-1 < n and 0 <= c-d1+d2-1 < n:
        if 0 <= c-d1 and c+d2 < n and r+d1+d2 < n:
            calculate(r, c, d1, d2)

for r in range(n-2):
    for c in range(1, n-1):
        for d1 in range(1, n-1):
            for d2 in range(1, n-1):
                check(r, c, d1, d2)
print(answer)
