// Lv.0 문자 리스트를 문자열로 변환하기

// 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/181941


// 풀이 1
#include <stdio.h>
#include <stdlib.h>

char* solution(const char* arr[], size_t arr_len) {
    char* answer = (char*)malloc(arr_len+1);
    for (int i=0; i<arr_len; i++){
        answer[i] = *arr[i];
    }
    answer[arr_len] = '\0';
        
    return answer;
}


// 풀이 2
#include <stdio.h>
#include <stdlib.h>

char* solution(const char* arr[], size_t arr_len) {
    char* answer = (char*)malloc(arr_len+1);
    for (int i=0; i<arr_len; i++){
        answer[i] = arr[i][0];
    }
    answer[arr_len] = '\0';
        
    return answer;
}