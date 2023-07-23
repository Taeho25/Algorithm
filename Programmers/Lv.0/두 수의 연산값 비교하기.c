// Lv.0 두 수의 연산값 비교하기

// 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/181938


// 풀이 1
#include <stdio.h>
#include <string.h>

int solution(int a, int b) {
    char str_ab[11], str_b[6];
    sprintf(str_ab, "%d", a);
    sprintf(str_b, "%d", b);
    strcat(str_ab, str_b);
    int ab = atoi(str_ab);
    
    return (ab >= 2*a*b) ? ab : 2*a*b;
}