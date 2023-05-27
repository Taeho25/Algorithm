'''Lv.0 주사위 게임 3'''

# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/181916


# 풀이 1
from itertools import combinations
def solution(a, b, c, d):
    numbers = [a, b, c, d]
    
    if a==b and b==c and c==d:
        return 1111*a
    
    for p1, p2, p3 in combinations(numbers, 3):
        q = [q for q in numbers if q not in [p1, p2, p3]]
        if len(q)==1: q1 = q[0]
        else: continue
        if p1==p2 and p2==p3 and p1!=q1:
            return (10*p1+q1)**2
    
    for p1, p2 in combinations(numbers, 2):
        q = [q for q in numbers if q not in [p1, p2]]
        if len(q)==2: q1, q2 = q[0], q[1]
        else: continue
        if p1==p2 and q1==q2 and p1!=q1:
            return (p1+q1)*abs(p1-q1)
        elif p1==p2 and q1!=q2 and p1!=q1 and p1!=q2:
            return q1*q2
        
    if len(numbers) == len(set(numbers)):
        return min(numbers) 
    

# 풀이 2
def solution(a, b, c, d):
    if a==b==c==d:       return 1111*a
    elif a==b==c:        return (10*a + d)**2
    elif a==b==d:        return (10*a + c)**2
    elif a==c==d:        return (10*a + b)**2
    elif b==c==d:        return (10*b + a)**2
    elif a==b and c==d:  return (a+c)*abs(a-c)
    elif a==c and b==d:  return (a+b)*abs(a-b)
    elif a==d and b==c:  return (a+b)*abs(a-b)
    elif a==b:           return c*d
    elif a==c:           return b*d
    elif a==d:           return b*c
    elif b==c:           return a*d
    elif b==d:           return a*c
    elif c==d:           return a*b
    else:                return min(a,b,c,d)


# 풀이 3
def solution(a, b, c, d):
    l = [a,b,c,d]
    c = [l.count(x) for x in l]
    
    if max(c) == 4:
        return 1111*a
    elif max(c) == 3:
        return (10*l[c.index(3)]+l[c.index(1)])**2
    elif max(c) == 2:
        if min(c) == 1:
            tmp = [x for x in l if l.count(x)==1]
            return tmp[0]*tmp[1]
        else:
            return (max(l) + min(l)) * abs(max(l) - min(l))
    else:
        return min(l)