# 한 마을에 모험가가 N명
# 모험가 길드에서는 N명의 모험가를 대상으로 공포도 측정
# 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 여행가능
# N명의 모험가에 대한 정보가 주어졌을 때, 여행을 떠날 수 있는 그룹 수의 최댓값

n = int(input())
number = list(map(int, input().split()))
number.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in number:
    count += 1 
    if count >= i:
        result += 1
        count = 0

print(result)




