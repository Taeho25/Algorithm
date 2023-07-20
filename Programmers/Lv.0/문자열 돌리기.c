// Lv.0 문자열 돌리기

// 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/181945


// 풀이 1
#include <stdio.h>
#define LEN_INPUT 11

int main(void) {
    char s1[LEN_INPUT];
    scanf("%s", s1);
    
    int i = 0;
    while(s1[i]){
        printf("%c\n", s1[i]);
        i++;
    }

    return 0;
}
