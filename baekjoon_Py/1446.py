# 학교에 가기 위해 차를 타고 D 킬로미터 길이의 고속도로를 지남
# 고속도로는 심각하게 커브가 많아서 운전하기가 힘듬
# 세준이는 이 고속도로에 지름길이 존재한다는 것을 알게됨
# 모든 지름길은 일반통행이고, 고속도로는 역주행 불가능
# 세준이가 운전해야 할 최솟값 출력
# 1. dp
import sys
input = sys.stdin.readline
N, D = map(int, input().split())    
dp = [i for i in range(D+1)]
lst = []
for _ in range(N):
    st, ne, lo = map(int, input().split())
    if ne - st > lo: # 일반 고속도로보다 더 빠른 경로인 경우
        lst.append((st,ne,lo))      
lst.sort()

for st, ne, lo in lst: # 각 지름길에 대해
    for i in range(1, D+1): 
        if ne == i:
            dp[i] = min(dp[i], dp[st]+lo) # 지름길을 이용할 경우
        else:
            dp[i] = min(dp[i], dp[i-1]+1) # 일반 고속도로를 이용할 경우
print(dp[D])
    
