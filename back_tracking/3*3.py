list_matrix = [[2, 4, 3], [1, 3, 7], [6, 5, 6]] # 3*3 정렬 입력값
check = [False]*3 # 열 선택 여부 처리

def back_tracking(row, score):
    if row == 3: # 종료 조건: 3개의 숫자를 선택했을 때
        print(score)
        return
    
    for col in range(3): # 현재 행에서 순회
        if not check[col]: # 아직 선택되지 않은 열이라면
            check[col] = True
            back_tracking(row+1, score+list_matrix[row][col])
            check[col] = False

back_tracking(0,0)