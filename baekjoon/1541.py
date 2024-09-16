# 양수, +, -, (, ) 가지고 식을 만들었다.
# 괄호를 모두 지웠다.
# 괄호를 적절히 쳐서 이 식의 값을 최소로 만들었다.
# 55-50+40 -> 55-50-40 = -35
# 10+20+30+40 -> 10+20+30+40 = 100
# 00009-00009 -> 00009-00009 = 0
import sys
input = sys.stdin.readline

a = input().split('-') # '-'를 기준으로 split해서 a 리스트에 저장

lst = [] # '-'로 나눈 항들의 합을 저장할 리스트

for i in a:
  sum = 0
  tmp = i.split('+') # 덧셈을 하기 위해 '+'를 기준으로 split
  for j in tmp: # split한 리스트의 각 요소들을 더해줌
    sum += int(j)
  lst.append(sum) # 각 항의 연산 결과(덧셈)를 lst에 저장

n = lst[0] # 식의 제일 처음은 숫자로 시작하기 때문에 0번째 값에서 나머지 값들을 빼준다

for i in range(1, len(lst)): # 1번째 값부터 n에서 빼준다.
  n -= lst[i]
print(n)