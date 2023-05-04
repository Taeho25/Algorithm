'''Lv.1 키패드 누르기'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/67256


# 풀이 1
def solution(numbers, hand):
    answer = ''
    pos = [(3, 1), 
           (0, 0), (0, 1), (0, 2),
           (1, 0), (1, 1), (1, 2),
           (2, 0), (2, 1), (2, 2),
           (3, 0),         (3, 2)]
    left = [1, 4, 7]
    right = [3, 6, 9]
    lhand = 10  # '*'
    rhand = 11  # '#'
    
    for number in numbers:
        if number in left:
            lhand = number
            answer += 'L'
        elif number in right:
            rhand = number
            answer += 'R'
        else:
            l_distance = abs(pos[lhand][0] - pos[number][0]) + abs(pos[lhand][1] - pos[number][1])
            r_distance = abs(pos[rhand][0] - pos[number][0]) + abs(pos[rhand][1] - pos[number][1])
            if l_distance < r_distance:
                lhand = number
                answer += 'L'
            elif l_distance > r_distance:
                rhand = number
                answer += 'R'
            else:
                if hand == 'left':
                    lhand = number
                    answer += 'L'
                else:
                    rhand = number
                    answer += 'R'
            
    return answer


# 풀이 2
def solution2(numbers, hand):
    answer = ''
    pos = {1:(0, 0),   2:(0, 1),   3:(0, 2),
           4:(1, 0),   5:(1, 1),   6:(1, 2),
           7:(2, 0),   8:(2, 1),   9:(2, 2),
           '*':(3, 0), 0:(3, 1), '#':(3, 2)}
    left = [1, 4, 7]
    right = [3, 6, 9]
    lhand = '*'
    rhand = '#'
    
    for number in numbers:
        if number in left:
            lhand = number
            answer += 'L'
        elif number in right:
            rhand = number
            answer += 'R'
        else:
            l_distance = abs(pos[lhand][0] - pos[number][0]) + abs(pos[lhand][1] - pos[number][1])
            r_distance = abs(pos[rhand][0] - pos[number][0]) + abs(pos[rhand][1] - pos[number][1])
            if l_distance < r_distance:
                lhand = number
                answer += 'L'
            elif l_distance > r_distance:
                rhand = number
                answer += 'R'
            else:
                if hand == 'left':
                    lhand = number
                    answer += 'L'
                else:
                    rhand = number
                    answer += 'R'
            
    return answer