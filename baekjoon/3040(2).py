# 완탐
data = [0] * 9
for i in range(9):
    data[i] = int(input())
sum = sum(data)

for j in range(9):
    for k in range(j+1, 9):
        if sum - (data[j]+data[k]) == 100:
            x, y = j, k
            break

data.pop(x)
data.pop(y-1)
for i in data:
    print(i)
