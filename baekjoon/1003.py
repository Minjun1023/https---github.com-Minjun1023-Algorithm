# 테스트 케이스를 입력받음.
T = int(input())
# dp, zero_count, one_count 초기화(N <= 40)
dp = [-1] * 41
zero_count = [0] * 41
one_count = [0] * 41

# fibo(0) = 0, fibo(1) = 1 고정값
dp[0] = 0
dp[1] = 1

# zero, one 개수 초기화
zero_count[0] = 1
one_count[1] = 1

# 재귀함수 
def fibo(n):
  # fibo의 값이 -1일 경우 아무것도 출력하지 않음
  if dp[n] != -1:
    return
  # fibo(2)부터 fibo(n)까지
  for i in range(2, n+1):
    # 점화식 fibo(n) = fibo(n-2) + fibo(n-1)
    dp[i] = dp[i-2] + dp[i-1]
    zero_count[i] = zero_count[i-2] + zero_count[i-1]
    one_count[i] = one_count[i-2] + one_count[i-1]

# T줄에 해당하는 N을 입력받음
for i in range(T):
  n = int(input())
  # 재귀함수 호출
  fibo(n)
  # 결과값 출력
  print(zero_count[n], one_count[n])
  