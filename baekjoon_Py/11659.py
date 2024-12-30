import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
sum = [0] # 구간합을 맞추기 위해 맨 처음 리스트 값을 0으로 지정

temp = 0
# 합 구하기
for i in nums:
  temp += i
  sum.append(temp)

# i, j 입력받고 구간값 결과 출력하기
for _ in range(M):
  i, j = map(int, input().split())
  print(sum[j]- sum[i-1])