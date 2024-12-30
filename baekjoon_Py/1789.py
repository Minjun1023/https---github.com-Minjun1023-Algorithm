s = int(input())
i = 0
cnt = 0

while True:
    # s가 i보다 클 경우(같아도 안됨)
    if s > i:
        # 1씩 차례대로 증가하면서
        i += 1
        # s값에서 i값을 빼고
        s -=i
        # 카운트 처리
        cnt += 1
    else:
        # 지금까지 카운트 처리한 값을 출력
        print(cnt)
        # 멈춤
        break
