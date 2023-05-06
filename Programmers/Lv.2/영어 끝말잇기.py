'''Lv.1 영어 끝말잇기'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12981


# 풀이 1
def solution(n, words):
    turn = 0
    person = 1
    answer = [0, 0]
    
    for p in range(1, len(words)): # 두 번째 사람 단어부터 확인
        turn = p // n + 1
        person = p % n + 1
        
        if (words[p] in words[:p]) or (words[p][0] != words[p-1][-1]):
            answer[0] = person
            answer[1] = turn
            break

    return answer


# 풀이 2
def solution(n, words):
    answer = [0, 0]
    
    for p in range(1, len(words)):       
        if (words[p] in words[:p]) or (words[p][0] != words[p-1][-1]):
            answer[0] = p % n + 1
            answer[1] = p // n + 1
            break

    return answer


# 풀이 3
def solution(n, words):
    for p in range(1, len(words)):       
        if (words[p] in words[:p]) or (words[p][0] != words[p-1][-1]):
            return [p % n + 1, p // n + 1]
        else:
            return [0, 0]