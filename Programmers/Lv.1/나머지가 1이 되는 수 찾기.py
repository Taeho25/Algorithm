'''Lv.1 나머지가 1이 되는 수 찾기'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/87389


# 풀이 1
def solution(n):
    answer = 0
    for x in range(2, n):
        if n % x == 1:
            answer = x
            break
    
    return answer


# ps. 1번 테케의 정답 숫자가 커서 시간이 오래 걸린다..