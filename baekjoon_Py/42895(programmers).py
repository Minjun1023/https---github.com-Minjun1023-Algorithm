# if n == 3:
# n을 1번 사용할 경우: {3}
# n을 2번 사용할 경우: {33},{3+3},{3-3},{3/3},{3*3}  -> {33,6,0,1,9}
# n을 3번 사용할 경우: 3,3,3을 사용 -> 1. 3+3,3 사용 2. 3-3,3 사용 3. 3/3,3 사용 4. 3*3,3 사용      33,3을 사용 -> 33*3,33-3,33+3,33/3,3*33,3-33,3+33,3/33
# n을 3번 사용했을 때 결과값 1. n을 1번 사용, n을 2번 사용 2. n을 2번 사용, n을 1번 사용
# n을 4번 사용할 경우: 1.n을 1번사용(연산)n을 3번사용 2. n을 2번사용(연산)n을 2번사용 3. n을 3번사용(연산)n을 1번사용
# 자료구조=set 중복 허용x

import sys
from itertools import product
input = sys.stdin.readline

def solution(N, number):
    answer = 1
    
    # DP[k] : N을 k번 써서 나타낼 수 있는 수의 집합
    DP = [set() for _ in range(9)]
    DP[1].add(N)
    
    if N == number:
        return answer
    
    # N을 cal_cnt번 써서 만들 수 있는 수를 구해서 DP에 저장
    # 그 과정에서 number와 같은 수를 만들 수 있다면 바로 answer 리턴
    for cal_cnt in range(2, 9):
        answer += 1
        # N을 cal_cnt번 이어붙여 만든 수
        DP[cal_cnt].add(int(str(N)*cal_cnt))
        
        # DP[N] = DP[i] (사칙연산) DP[N-i] (1 <= i <= N-1)
        for i in range(1, cal_cnt):
            j = cal_cnt - i
            
            # 데카르트 곱
            for x, y in product(DP[i], DP[j]):
                DP[cal_cnt].update({x+y, x-y, x*y})
                
                if y != 0:
                    DP[cal_cnt].add(x//y)
            
            if number in DP[cal_cnt]:
                return answer
        
    return -1