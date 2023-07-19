// Lv.0 문자열 반복해서 출력하기

// 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/181950


// 풀이 1
#include <stdio.h>
#define LEN_INPUT 11

int main(void) {
    char s1[LEN_INPUT];
    int a;
    
    scanf("%s %d", s1, &a);
    
    for (size_t i=0; i<a; i++) printf("%s", s1);
    
    return 0;
}