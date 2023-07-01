'''Lv.2 개인정보 수집 유효기간'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/150370


# 풀이 1
def solution(today, terms, privacies):
    answer = []
    time_dict = dict()
    year, month, day = int(today[0:4]), int(today[5:7]), int(today[8:])
    
    for term in terms : 
        case = term[0]
        time_dict[case] = int(term[2:])
    
    for i in range(len(privacies)):
        date, case = privacies[i].split()
        p_year, p_month, p_day = int(privacies[i][0:4]), int(privacies[i][5:7]), int(privacies[i][8:10])
        
        p_month += time_dict[case]
        
        while p_month > 12 : 
            p_month -= 12
            p_year +=1
            
            
        if p_year > year :
            continue
            
        elif p_year == year :
            if p_month > month :
                continue
                
            elif p_month == month :
                if p_day > day :
                    continue
                    
        answer.append(i+1)
    
    return answer