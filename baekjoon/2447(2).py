# 풀이 2: 공간을 1, 2, 3으로 나눈 후 재귀함수를 통해 구해진 별을 붙임.
import sys
sys.setrecursionlimit(10**6) # 재귀함수 깊이 조정
input = sys.stdin.readline

n = int(input().strip())

def append_star(LEN):
    if LEN == 1: 
        return ['*']
    
    Stars = append_star(LEN//3)
    L = []

    for S in Stars:
        L.append(S*3)
    for S in Stars:
        L.append(S+' '*(LEN//3)+S)
    for S in Stars:
        L.append(S*3)
    return L

print('\n'.join(append_star(n)))