'''Lv.2 [3차] n진수 게임'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/17687


# 풀이 1 : 튜브 숫자 바로바로 찾기
def solution(n, t, m, p):
    answer = ''
    num_str = ''
    over_10 = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    
    for num in range(100000):
        #print(num)
        
        # 1. n진수 변환, num_str에 붙이기
        n_num = '0' if num == 0 else ''
        while(num > 0):
            if num % n < 10:
                n_num = str(num % n) + n_num
            else:
                n_num = over_10[(num % n)] + n_num
            num //= n
        num_str += n_num
        #print("step 1:", num_str)
        
        # 2. 숫자 개수 m개 초과시 튜브 숫자 찾기
        if len(num_str) > m:
            answer += num_str[p-1]
            num_str = num_str[m:]
        #print("step 2:", num_str)
    
        # 3. 튜브 숫자 t개 모이면 종료
        #print("step 3:", answer)
        if len(answer) == t:
            break
    
    return answer


# 풀이 2 : 전체 문자열 생성 후 튜브 숫자들 찾기
def solution(n, t, m, p):
    answer = ''
    num_str = '0'
    over_10 = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    
    for num in range(1, 100000):
        if len(num_str) >= t*m: break
        
        n_num = ''
        while(num):
            if num % n < 10:
                n_num = str(num % n) + n_num
            else:
                n_num = over_10[(num % n)] + n_num
            num //= n
        num_str += n_num

    answer = num_str[p-1::m][:t]
    
    return answer


# 풀이 3 : 0123456789ABCDEF
def solution(n, t, m, p):
    answer = ''
    num_str = '0'
    nn = "0123456789ABCDEF"
    
    for num in range(1, 100000):
        if len(num_str) >= t*m: break
        
        n_num = ''
        while(num):
            n_num = nn[num % n] + n_num
            num //= n
        num_str += n_num

    answer = num_str[p-1::m][:t]
    
    return answer


# 풀이 4 : divmod
def solution(n, t, m, p):
    answer = ''
    num_str = '0'
    nn = "0123456789ABCDEF"
    
    for num in range(1, 100000):
        if len(num_str) >= t*m: break
        
        n_num = ''
        while(num):
            num, remainder = divmod(num, n)
            n_num = nn[remainder] + n_num
        num_str += n_num

    answer = num_str[p-1::m][:t]
    
    return answer


# 풀이 5 : for문 범위 지정, 정답 바로 반환
def solution(n, t, m, p):
    num_str = '0'
    nn = "0123456789ABCDEF"
    
    for num in range(1, t*m):        
        n_num = ''
        while(num):
            num, remainder = divmod(num, n)
            n_num = nn[remainder] + n_num
        num_str += n_num

    return num_str[p-1::m][:t]