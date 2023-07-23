// Lv.0 더 크게 합치기

// 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/181939


// 풀이 1
#include <stdio.h>
#include <string.h>
#include <math.h>

int solution(int a, int b) {
    char str_a[6];
    char str_b[6];
    sprintf(str_a, "%d", a);
    sprintf(str_b, "%d", b);
    int len_a = strlen(str_a);
    int len_b = strlen(str_b);
    
    if (a * pow(10, len_b) + b > b * pow(10, len_a) + a)
        return a * pow(10, len_b) + b;
    else
        return b * pow(10, len_a) + a;
}


// 풀이 2
#include <stdio.h>
#include <string.h>

int solution(int a, int b) {
    char str_a[6], str_b[6];
    char str_ab[11], str_ba[11];
    sprintf(str_a, "%d", a);
    sprintf(str_b, "%d", b);
    sprintf(str_ab, "%d", a);
    sprintf(str_ba, "%d", b);
    
    strcat(str_ab, str_b);
    strcat(str_ba, str_a);
    
    return (atoi(str_ab) > atoi(str_ba)) ? atoi(str_ab) : atoi(str_ba);
}