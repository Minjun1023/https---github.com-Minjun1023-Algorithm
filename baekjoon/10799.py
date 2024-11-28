ans = input() # 괄호를 입력받음
stack = [] # stack 배열 생성
cnt = 0 # 막대기 갯수

for i in range(len(ans)):
    # 열린 괄호일 경우 스택에 추가
    if ans[i] == "(":
        stack.append("(")
    # 닫힌 괄호일 경우
    else:
        # 닫힌 괄호 이전이 열린 괄호일 경우 pop해서 스택의 길이만큼 카운트 값에 더해줌.
        if ans[i-1] == "(":
            stack.pop()
            cnt += len(stack)
        # 닫힌 괄호가 연속으로 나올 경우 카운트 값에 1을 더해줌.
        else:
            stack.pop()
            cnt += 1
# 결과값 출력
print(cnt)
        


