// Lv.0 문자열 곱하기

// 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/181940


// 풀이 1
#include <stdio.h>
#include <string.h>

char* solution(const char* my_string, int k) {
    int len = strlen(my_string);
    char* answer = (char*)malloc(len*k+1);
    
    for (int i=0; i<k; i++){
        memcpy(&answer[len*i], my_string, len);
    }
    answer[len*k] = '\0';

    return answer;
}