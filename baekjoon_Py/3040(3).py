# 집합
import sys
from itertools import combinations
input = sys.stdin.readline

def solve(case):
    if sum(case) == 100:
        case = list(case)
        case.sort()
        for i in case:
            print(int(i))
        return True
    return False

if __name__ == "__main__":
    data=set()
    for i in range(9):
        height = int(input().strip())
        data.add(height)

    for case in combinations(data, 7):
        if solve(case):
            break