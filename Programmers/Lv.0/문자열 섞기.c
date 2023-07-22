// Lv.0 문자열 섞기

// 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/181942


// 풀이 1
#include <stdio.h>
#include <stdlib.h>

char* solution(const char* str1, const char* str2) {
    char* answer = (char*)malloc(10*2+1);
    int len = strlen(str1);
    
    for (size_t i=0; i<len; i++){
        answer[i*2] = str1[i];
        answer[i*2+1] = str2[i];
    }
    answer[len*2] = '\0';
    
    return answer;
}