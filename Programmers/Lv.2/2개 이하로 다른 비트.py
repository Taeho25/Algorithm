'''Lv.2 2개 이하로 다른 비트'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/77885


# 풀이 1 : 테케 10, 11 시간초과
def solution(numbers):
    answer = []
    
    for number in numbers:
        x_bin = bin(number)[2:]
        while True:
            # 1. x, x2 전처리
            number += 1
            x2_bin = bin(number)[2:]
            if len(x_bin) != len(x2_bin):
                x_bin = '0' + x_bin
                
            # 2. 비교
            dif_cnt = sum([1 for x_bit, x2_bit in zip(x_bin, x2_bin) if x_bit != x2_bit])
                    
            # 3. 목표값이면 저장, 반복문 탈출
            if dif_cnt <= 2:
                answer.append(number)
                break
    
    return answer


# 풀이 2
def solution(numbers):
    answer = []

    for number in numbers:
        # 1. 가장 뒤의 0의 인덱스를 1로 바꾸기
        x_bin = list('0' + bin(number)[2:])
        idx = ''.join(x_bin).rfind('0')
        x_bin[idx] = '1'
        
        # 2. 홀수면 그 다음 인덱스를 0으로 바꾸기
        if number % 2 == 1:
            x_bin[idx+1] = '0'
        
        # 3. 목표값 저장
        answer.append(int(''.join(x_bin), 2))  # int(number, 2) : 2진수인 number를 10진수로 바꿈

    return answer