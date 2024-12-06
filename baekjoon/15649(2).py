# 백트래킹
def back_tracking(start):
    # arr배열의 길이가 m이면 출력
    if len(arr) == m:
        print(*arr)
        return

    for i in range(start,n+1):
        if i not in arr:
            arr.append(i)
            # 1,2 2,1은 중복으로 간주하기 때문에 호출함수에 i+1을 해서 2,3이 출력이 되도록 설정
            back_tracking(i+1)
            # arr배열의 길이가 m이면 출력 이후 pop()을 해서 제일 앞에 있는 값을 보존
            arr.pop()

n, m = list(map(int, input().split()))
arr = []

back_tracking(1)

