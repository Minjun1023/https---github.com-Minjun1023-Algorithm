# N X N 크기의 정사각형 모양의 종이
# N/2 X N/2 크기로 나눈다.(잘라진 종이가 모두 하얀색 또는 모두 파란색으로 칠해져 있거나, 하나의 정사각형 칸이 되어 더 이상 자를 수 없을 때 까지 반복)
import sys
input = sys.stdin.readline

N = int(input()) # 전체 종이의 한 변의 길이 N을 입력받음
paper = [list(map(int, input().split())) for _ in range(N)] # N X N 크기의 정사각형의 입력값을 paper에 저장

result = [] # 하얀색, 파란색 색종이 개수를 출력하기 위해 

def solution(x, y, N):
  color = paper[x][y] # 하얀색, 파란색 색종이를 구별하기 위해 사용
  for i in range(x, x+N):
    for j in range(y, y+N):
      if color != paper[i][j]: # 잘라진 종이가 하얀색, 파란색 종이로 채워지지 않은 경우
        solution(x, y, N//2)
        solution(x, y+N//2, N//2)
        solution(x+N//2, y, N//2)
        solution(x+N//2, y+N//2, N//2)
        return
  if color == 0: # 하얀색 종이
    result.append(0)
  else: # 파란색 종이
    result.append(1)

solution(0,0,N)
print(result.count(0)) # 하얀색 종이 개수 출력
print(result.count(1)) # 파란색 종이 개수 출력