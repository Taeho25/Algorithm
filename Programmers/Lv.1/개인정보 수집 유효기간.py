'''Lv.1 개인정보 수집 유효기간'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/150370


# 풀이 1
def solution(today, terms, privacies):
    answer = []
    
    # 1. today 숫자 세팅
    today = int("".join(today.split('.')))
    
    # 2. 약관종류-유효기간 딕셔너리화
    time_dict = {}
    for term in terms:
        _type, _term = term.split()
        _m = int(_term) // 12
        _d = int(_term) % 12
        time_dict[_type] = (_m, _d)
    #print(ttype)
    
    # 3. 개인정보 수집일자 처리
    for i, privacy in enumerate(privacies):
        _date, _type = privacy.split()
        _year, _month, _day = map(int, _date.split('.'))

        _year = _year + time_dict[_type][0]
        _month += time_dict[_type][1]
        if _month > 12:
            _year += 1
            _month -= 12
        
        _date_limit = _year*10000 + _month*100 + _day
        
        if today >= _date_limit:
            answer.append(i+1)    
    
    return answer


# 풀이 2
def solution(today, terms, privacies):
    answer = []

    # 1. today 숫자 세팅
    year, month, day = map(int, today.split('.'))
    
    # 2. 약관종류-유효기간 딕셔너리화
    time_dict = dict()
    for term in terms:
        _type, _term = term.split()
        time_dict[_type] = int(_term)

    # 3. 개인정보 수집일자 처리
    for i, privacy in enumerate(privacies):
        _date, _type = privacy.split()
        _year, _month, _day = map(int, _date.split('.'))
        
        _month += time_dict[_type]
        
        while _month > 12: 
            _month -= 12
            _year +=1
            
        if _year > year:
            continue
        elif _year == year:
            if _month > month :
                continue   
            elif _month == month :
                if _day > day :
                    continue
                    
        answer.append(i+1)
    
    return answer


# 풀이 3
def solution(today, terms, privacies):
    answer = []

    # 1. today 세팅
    year, month, day = map(int, today.split('.'))
    today_day = year*12*28 + month*28 + day
    
    # 2. 약관종류-유효기간 딕셔너리화
    time_dict = dict()
    for term in terms:
        _type, _term = term.split()
        time_dict[_type] = int(_term)*28

    # 3. 개인정보 수집일자 처리
    for i, privacy in enumerate(privacies):
        _date, _type = privacy.split()
        _year, _month, _day = map(int, _date.split('.'))
        _date_day = _year*12*28 + _month*28 + _day + time_dict[_type]
        
        if today_day >= _date_day:
            answer.append(i+1)
    
    return answer


# 풀이 4
def to_days(date):
    year, month, day = map(int, date.split("."))
    return year*12*28 + month*28 + day

def solution(today, terms, privacies):
    answer = []
    time_dict = {t[0]: int(t[2:])*28 for t in terms}
    today = to_days(today)
    
    for i, privacy in enumerate(privacies):
        date = to_days(privacy[:-2]) + time_dict[privacy[-1]]
        if today >= date:
            answer.append(i+1)
    
    return answer


# 풀이 5
def to_days(date):
    year, month, day = map(int, date.split("."))
    return year * 28 * 12 + month * 28 + day

def solution(today, terms, privacies):
    months = {v[0]: int(v[2:]) * 28 for v in terms}
    today = to_days(today)
    expire = [
        i + 1 for i, privacy in enumerate(privacies)
        if to_days(privacy[:-2]) + months[privacy[-1]] <= today
    ]
    return expire
