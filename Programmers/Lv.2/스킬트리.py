'''Lv.2 스킬트리'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/49993


# 풀이 1
def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        user_skill = "".join([sk for sk in skill_tree if sk in skill])
        
        if skill[:len(user_skill)] == user_skill:
            answer += 1
    
    return answer


# 풀이 2
def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        skill_list = list(skill)

        for sk in skill_tree:
            if sk in skill:
                if sk != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer


# 풀이 3
def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        user_skill = ""
        
        for sk in skill_tree:
            if sk in skill:
                user_skill += sk
        
        if user_skill == skill[:len(user_skill)]:
            answer += 1
            
    return answer