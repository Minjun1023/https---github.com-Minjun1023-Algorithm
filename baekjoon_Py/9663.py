# back_tracking
import sys
input = sys.stdin.readline

# input
N = int(input())
maps = [[0] * N  for _ in range(N)]
# 열 점유 여부
check = [False] * N
# y=x 점유 여부
check_up = [False]*(2*(N-1)+1)
# y=-x 점유 여부
check_down = [False]*(2*(N-1)+1)

cnt = 0

def N_Queen(k):
    global N, cnt

    # 퀸의 갯수가 줄의 수와 같으면(1줄:1개)
    if k == N:
        cnt += 1
        return
    
    for i in range(N):
        # 방문을 안했을 경우
        if not check[i] and not check_up[k+i] and not check_down[(N-1)+k-i]:
            # 방문처리 이후
            check[i] = True
            check_up[k+i] = True
            check_down[(N-1)+k-i] = True
            # 값 추가
            N_Queen(k+1)
            # 미 방문으로 처리
            check[i] = False
            check_up[k+i] = False
            check_down[(N-1)+k-i] = False

# output
N_Queen(0)
print(cnt)