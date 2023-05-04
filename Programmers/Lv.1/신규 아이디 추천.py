'''Lv.1 신규 아이디 추천'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/72410


# 풀이 1
def solution(new_id):
    using_word = "0123456789abcdefghijklmnopqrstuvwxyz-_."
    
    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    new_id = [w for w in new_id if w in using_word]
    new_id = "".join(new_id)
    
    # 3단계
    while ('..' in new_id):
        new_id = new_id.replace('..', '.')
    
    # 4단계
    if len(new_id) > 0:
        if new_id[0] == '.':
            new_id = new_id[1:]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    
    # 5단계
    if new_id == "": new_id = "aaa"
    
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.': new_id = new_id[:-1]
        
    # 7단계
    while len(new_id) <= 2:
        new_id += new_id[-1]
    
    return new_id