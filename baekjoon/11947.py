t = int(input())
# 중간값 지정(최대값)
mid = 1
for _ in range(t):
    a = int(input())
    # 입력 받은 수의 중간값 계산
    mid = (5*(10**(len(str(a)) - 1)))
    # 입력 받은 수가 중간값보다 작을 경우 
    if mid > a:
        mid = 0
    # 클 경우
    else:
        mid = mid*(mid-1)
    # 반전 값 배열
    r_a = []
    # 입력 받은 수를 자릿수마다 순회(9씩 빼줌)
    for i in list(str(a)):
        r_a.append(str(9-int(i)))
    # 값을 int 형으로 저장
    r_a = int(''.join(r_a))
    res = a*r_a
    # 최댓값을 찾는 과정 결과값 > 중간값인 경우 결과값 출력
    if res > mid:
        print(res)
    # 아닌 경우 중간값 출력
    else:
        print(mid)


