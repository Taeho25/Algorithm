'''Lv.1 [1차] 다트 게임'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/17682


# 풀이 1
def solution(dartResult):
    number = ''
    bonus = ['', 'S', 'D', 'T']
    answer = [0]
    turn = 0
    
    for data in dartResult:
        if '0' <= data and data <= '9':
            number += data
        elif data in bonus:
            answer.append(pow(int(number), bonus.index(data)))
            number = ''
            turn += 1
        elif data == '*':
            answer[turn - 1] *= 2
            answer[turn] *= 2
        elif data == '#':
            answer[turn] *= -1

    return sum(answer)

  
# 풀이 2
def solution2(dartResult):
    dartResult = dartResult.replace('10','k')
    dartResult = ['10' if i == 'k' else i for i in dartResult]
    #print(dartResult)
    bonus = ['S', 'D', 'T']
    answer = []
    turn = -1
    
    for data in dartResult:
        if '0' <= data and data <= '9':
            answer.append(int(data))
            turn += 1
        elif data in bonus:
            answer[turn] = answer[turn] ** (bonus.index(data)+1)
        elif data == '*':
            answer[turn] *= 2
            if turn != 0 : answer[turn - 1] *= 2
        elif data == '#':
            answer[turn] *= -1

    return sum(answer)