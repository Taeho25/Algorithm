'''Lv.1 시저 암호'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12926


# 풀이 1
def solution(s, n):
    answer = ''
    temp = ''
    for word in s:
        if word == ' ': answer += ' '
        else:
            temp = chr(ord(word) + n)
            if 'a' <= word and word <= 'z' and temp > 'z':
                temp = chr(ord(temp) - 26)
            elif 'A' <= word and word <= 'Z' and temp > 'Z':
                temp = chr(ord(temp) - 26)
            answer += temp        
        
    return answer


# 풀이 2
def solution2(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))

    return "".join(s)