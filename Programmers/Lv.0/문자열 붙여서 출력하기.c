// Lv.0 문자열 붙여서 출력하기

// 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/181946


// 풀이 1
#include <stdio.h>
#define LEN_INPUT1 11
#define LEN_INPUT2 11

int main(void) {
    char s1[LEN_INPUT1];
    char s2[LEN_INPUT2];
    scanf("%s %s", s1, s2);
    
    printf("%s%s", s1, s2);

    return 0;
}