// Lv.0 조건 문자열

// 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/181934


// 풀이 1
#include <stdio.h>

int solution(const char* ineq, const char* eq, int n, int m) {
    if (strcmp(ineq, ">") == 0){
        if (strcmp(eq, "=") == 0)
            return (n >= m);
        else
            return (n > m);
    }
    else{
        if (strcmp(eq, "=") == 0)
            return (n <= m);
        else
            return (n < m);
    }
}


// 풀이 2
#include <stdio.h>

int solution(const char* ineq, const char* eq, int n, int m) {
    if(*ineq == '>')
    {
        if(*eq == '=')
            return n >= m;
        else
            return n > m;
    }
    else
    {
        if(*eq == '=')
            return n <= m;
        else
            return n < m;
    }
}