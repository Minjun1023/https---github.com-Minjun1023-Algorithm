# 목표: 아홉 개의 수 중 합이 100이 되는 일곱 개의 수를 찾는다.
lst = []
for _ in range(9):
    lst.append(int(input()))
for i in range(9):
    for j in range(i+1, 9):
        # 전체 합에서 어떤 값을 뺄 경우 100이 나오는 경우
        if sum(lst) - lst[i] - lst[j] == 100:
            # 그 값을 x, y에 저장하고 중단
            x, y = i, j
            break

# 값을 pop() 해서 lst[]에서 없앰
# x번째 요소를 먼저 제거해서 리스트 길이가 1이 줄어들어 y-1을 해야함
lst.pop(x)
lst.pop(y-1)
# 출력
for i in lst:
    print(i)




