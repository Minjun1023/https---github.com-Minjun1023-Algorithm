import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    stick_len, ant_count = map(int, input().split())

    min_time = []
    max_time = []

    for _ in range(ant_count):
        # 현재 개미 위치
        loc = int(input())
        
        # 현재 개미가 땅으로 떨어지는 최소 시간
        min_time.append(min(loc, stick_len - loc))
        # 현재 개미가 땅으로 떨어지는 최대 시간
        max_time.append(max(loc, stick_len - loc))

    # 각 개미가 떨어지는 최소 시간 중 제일 큰 값과 최대 시간 중 제일 큰 값 출력
    print(max(min_time), max(max_time))
