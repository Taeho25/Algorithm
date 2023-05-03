'''Lv.1 숫자 문자열과 영단어'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/81301


# 풀이 1
def solution(s):
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    word = ""
    answer = []
    
    for w in s:
        word += w
        if '0' <= w and w <= '9':
            answer.append(w)
            word = ""
        elif word in numbers:
            n = str(numbers.index(word))
            answer.append(n)
            word = ""

    answer = "".join(answer)
    return int(answer)


# 풀이 2
def solution2(s):
    numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(numbers)):
        s = s.replace(numbers[i], str(i))

    return int(s)


# 풀이 3
def solution3(s):
    numbers_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

    for key, value in numbers_dic.items():
        s = s.replace(key, value)

    return int(s)