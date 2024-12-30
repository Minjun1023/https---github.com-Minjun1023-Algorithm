# random 함수
import random
data = [0] * 9
for i in range(9):
    data[i] = int(input())
result = 0

while result != 100:
    real = random.sample(data, 7)
    result = sum(real)

real = sorted(real)

for i in real:
    print(i)