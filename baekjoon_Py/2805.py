# 나무 M미터 필요
# 절단기에 높이 H 지정
# 높이 지정 시 톱날이 땅으로부터 H미터 위로 올라감
# H = 20, 15, 10, 17 일 경우 H = 15로 지정할 경우 나무를 자른 뒤 높이 = 15, 15, 10, 15 남은 5, 2 가져갈 수 있음. 총 7 
# 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree) # 초기 시작과 끝 값 설정

# 이분탐색

while start <= end:
  mid = (start + end) // 2 # 중간값 설정

  sum = 0 # 벌목된 나무 총합
  for i in tree:
    if i >= mid:
      sum += i - mid # 중간값을 기준으로 잘랐을 때 가져갈 수 있는 나무 길이 합 계산
  
  if sum >= M: # 벌목 높이를 이분탐색
    start = mid + 1
  else:
    end = mid - 1
print(end)
