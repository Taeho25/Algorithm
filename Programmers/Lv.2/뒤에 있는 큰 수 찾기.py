'''Lv.2 뒤에 있는 큰 수 찾기'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/154539


# 풀이 1 : 시간초과 O(N^2)
def solution(numbers):
    answer = [-1]*len(numbers)
    
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] < numbers[j]:
                answer[i] = numbers[j]
                break
        
    return answer


# 풀이 2 : stack 이용
def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)

    for i in range(len(numbers)):
            while stack and numbers[stack[-1]] < numbers[i]:
                answer[stack.pop()] = numbers[i]
            stack.append(i)
    
    return answer