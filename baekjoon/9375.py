import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    wears = {}
    n = int(input())
    for _ in range(n):
        name, type = input().strip().split()
        if type in wears: # 같은 종류의 의상이 있을 경우
            wears[type].append(name)
        else: # 없을 경우
            wears[type] = [name]
    
    cnt = 1

    for x in wears:
        cnt *= (len(wears[x]) + 1) # 종류의 의상을 착용해도 되고 안해도 되는 경우에서 (a 종류수 + 1) * (b 종류수 + 1) * (c 종류수 + 1) .. 
    
    print(cnt-1) # 모든 의상을 착용하지 않은 경우를 제외해야 하므로 -1

