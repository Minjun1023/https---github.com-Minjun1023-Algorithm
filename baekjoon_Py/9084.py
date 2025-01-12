# 화폐단위: 1, 5, 10, 100, 500원
# 출력: 동전의 종류가 주어질 때 주어진 금액을 만드는 모든 방법
# 2차원
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    coins.insert(0,0) # 동전 인덱스를 1부터 사용하기 위해 작성: coins[0, coins에 입력한 값]
    m = int(input())
    dp = [[0] * (m+1) for i in range(n+1)]
    for i in range(1, n+1):
        dp[i][0] = 1 # 0원을 만들 수 있는 경우는 전부 존재
    for j in range(1, n+1):
        for i in range(1, m+1):
            dp[j][i] = dp[j-1][i] # 이전까지의 경우의 수를 가져옴
            if i-coins[j] >= 0:
                dp[j][i] += dp[j][i-coins[j]]
    print(dp[n][m])

    


