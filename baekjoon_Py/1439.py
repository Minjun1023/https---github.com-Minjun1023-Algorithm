s = input()
cnt = 0

for i in range(len(s) - 1):
    if s[i]!=s[i+1]:
        cnt+=1
res = (cnt + 1) // 2
print(res)


