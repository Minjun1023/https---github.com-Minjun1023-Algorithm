import sys
input = sys.stdin.readline
def ccw(x1, y1, x2, y2, x3, y3):
    # 외적값 구하는 공식
    return x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
res = ccw(x1, y1, x2, y2, x3, y3)
# 외적값이 양수일 경우 
if res > 0:
    print(1)
# 외적값이 음수일 경우
elif res < 0:
    print(-1)
# 외적값이 0일 경우
else:
    print(0)