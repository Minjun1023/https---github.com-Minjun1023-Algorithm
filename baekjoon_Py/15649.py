# 순열, 조합 계산하기 위한 라이브러리
import itertools

n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]

# premutations 순열
arr = itertools.permutations(nums, m)

for i in arr:
    print(' '.join(map(str, i)))