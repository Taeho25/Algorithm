'''Lv.2 모음사전'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/84512


# 풀이 1
from itertools import product

def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    dict1 = [v for v in vowels]
    dict2 = [v1+v2 for v1, v2 in product(vowels, repeat=2)]
    dict3 = [v1+v2+v3 for v1, v2, v3 in product(vowels, repeat=3)]
    dict4 = [v1+v2+v3+v4 for v1, v2, v3, v4 in product(vowels, repeat=4)]
    dict5 = [v1+v2+v3+v4+v5 for v1, v2, v3, v4, v5 in product(vowels, repeat=5)]
    
    dictionary = dict1 + dict2 + dict3 + dict4 + dict5
    dictionary.sort()
    
    return dictionary.index(word) + 1


# 풀이 2
from itertools import product

def solution(word):
    dictionary = []
    
    for i in range(5):
        for c in product("AEIOU", repeat=i+1):
            dictionary.append("".join(c))
    dictionary.sort()
    
    return dictionary.index(word) + 1


# 풀이 3 : 등비수열의 합
def solution(word):
    answer = 0

    for i, n in enumerate(word):
        answer += (5 ** (5 - i) - 1) / (5 - 1) * "AEIOU".index(n) + 1
    
    return answer