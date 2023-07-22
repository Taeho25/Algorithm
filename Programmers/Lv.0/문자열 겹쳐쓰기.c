// Lv.0 문자열 겹쳐쓰기

// 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/181943


// 풀이 1
#include <stdio.h>
#include <string.h>

char* solution(const char* my_string, const char* overwrite_string, int s) {
    char* answer = (char*)malloc(1001);  // 동적할당, 길이+1
    memcpy(answer, my_string, sizeof(char)*1001);  // 문자열이 const 이므로 복사

    int i = 0;
    while(i < strlen(overwrite_string)){
        answer[s] = overwrite_string[i];
        s++;
        i++;
    }
    
    return answer;
}


// 풀이 2
#include <stdio.h>
#include <string.h>

char* solution(const char* my_string, const char* overwrite_string, int s) {
    char* answer = (char*)malloc(1001);  // 동적할당, 길이+1
    memcpy(answer, my_string, sizeof(char)*1001);  // 문자열이 const 이므로 복사
    memcpy(&answer[s], overwrite_string, strlen(overwrite_string));
    
    return answer;
}