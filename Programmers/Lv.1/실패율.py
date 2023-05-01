'''Lv.1 실패율'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/42889


# 풀이 1
def solution(N, stages):
    stage_num = [0]*(N+2)
    for stage in stages:
        stage_num[stage] += 1
    # print(stage_num)
    
    user = len(stages)
    failure_rate = []
    for idx in range(1, N+1):
        if stage_num[idx] == 0:
            failure_rate.append((idx, 0))
        else:
            f_rate = stage_num[idx] / user
            user -= stage_num[idx]
            failure_rate.append((idx, f_rate))
    # print(failure_rate)    
    
    fail_sort = sorted(failure_rate, key=lambda x: x[1], reverse=True)
    # print(fail_sort)
    answer = []
    for f in fail_sort:
        answer.append(f[0])
    
    return answer


# 풀이 2
def solution2(N, stages):    
    stage_num2 = [0] * (N + 2)
    for stage in stages:
        stage_num2[stage] += 1
    
    failure_rate2 = []
    for i in range(1, N+1):
        users = sum(stage_num2[i:])
        now_user = stage_num2[i]
        if users == 0:
            failure_rate2.append((i, 0))
        else:
            failure_rate2.append((i, now_user/users))
            
    fail_sort = sorted(failure_rate2, key=lambda x: x[1], reverse=True)
    answer = []
    for f in fail_sort:
        answer.append(f[0])
        
    return answer