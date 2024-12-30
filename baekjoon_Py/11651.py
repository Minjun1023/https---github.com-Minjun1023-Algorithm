# 입력
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# y값을 먼저 정렬한다음 만약 y값이 같다면, x값 끼리 비교해서 작은것을 먼저 출력
arr.sort(key=lambda x:(x[1], x[0]))

# 결과값 출력
for i in arr:
    print(i[0], i[1])
