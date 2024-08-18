import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 키, 값을 저장하기 위해 딕셔너리 사용
dict = {}

for i in range(1, N+1):
  a = input().rstrip()
  dict[i] = a
  dict[a] = i

for i in range(M):
  quest = input().rstrip()
  if quest.isalpha(): # 질문에 문자열에 알파벳 문자가 포함되어 있으면
    print(dict[quest]) 
  else: # 아니면
    print(dict[int(quest)])


