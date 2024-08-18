T = int(input())

# 계단의 숫자 초기화
stairs = [0] * 301
for i in range(1, T+1):
  stairs[i] = int(input())

# dp 배열 초기화
dp = [0] * 301
dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]
dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

# 점화식 계산 dp[i] = max(직전 칸, 전전 칸)
for i in range(4, T+1):
  dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2] + stairs[i])

print(dp[T])

