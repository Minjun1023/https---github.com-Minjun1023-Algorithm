import sys
input = sys.stdin.readline
T = int(input()) # 사용자에게 테스트 케이스 수를 입력받는다.

for _ in range(T): # T줄 만큼 정수 N을 입력받고 dp테이블을 초기화한다.
  N = int(input())
  dp = [0] * (N+1)

  for i in range(1, N+1): # i = 1, 2, 3일 경우 값일 경우와 그 외의 경우 점화식의 값을 사용해서 값을 구한다.
    if i == 1:
      dp[i] = 1
    elif i == 2:
      dp[i] = 2
    elif i == 3:
      dp[i] = 4
    else:
      dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
  # 결과값 출력    
  print(dp[N])