'''Lv.1 크레인 인형뽑기 게임'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/64061


# 풀이 1
def solution(board, moves):
    answer = 0
    hold = 0
    box = []
    top = -1
    
    for option in moves:
        # 집기
        for step in range(len(board)):  # 인형 있는 곳 까지 집게 내리기
            if board[step][option-1] != 0:  # 인형이 있으면
                hold = board[step][option-1]
                board[step][option-1] = 0
                break
        
        # 집은거 내려놓기
        if hold != 0:
            if top == -1:  # 빈 박스
                box.append(hold)
                top += 1
            else:          # 찬 박스
                if box[top] == hold:  # 같은 인형
                    box.pop()
                    answer += 2
                    top -= 1
                else:                 # 다른 인형
                    box.append(hold)
                    top += 1
            hold = 0
            
    return answer


# 풀이 2
def solution2(board, moves):
    answer = 0
    box = []
    
    for option in moves:
        for step in range(len(board)):  # 인형 있는 곳 까지 집게 내리기
            if board[step][option-1] != 0:
                box.append(board[step][option-1])
                board[step][option-1] = 0
                
                if len(box) > 1:  # 2개 이상
                    if box[-1] == box[-2]:
                        box.pop()
                        box.pop()
                        answer += 2
                break
            
    return answer