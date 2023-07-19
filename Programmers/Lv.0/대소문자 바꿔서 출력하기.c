// Lv.0 대소문자 바꿔서 출력하기

// 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/181949


// 풀이 1
#include <stdio.h>
#include <ctype.h>
#define LEN_INPUT 21

int main(void) {
    char s1[LEN_INPUT];
    int i = 0;

    scanf("%s", s1);
    
    while (s1[i]){
        if (isupper(s1[i])){
            s1[i] = tolower(s1[i]);
        }
        else if (islower(s1[i])){
            s1[i] = toupper(s1[i]);
        }
        i++;
    }

    printf("%s", s1);

    return 0;
}


// 풀이 2
#include <stdio.h>
#define LEN_INPUT 21

int main(void) {
    char s1[LEN_INPUT];
    int i = 0;

    while (s1[i]){
        if (s1[i] >= 'A' && s1[i] <= 'Z'){
            s1[i] += 32;
        }
        else if (s1[i] >= 'a' && s1[i] <= 'z'){
            s1[i] -= 32;
        }
        i++;
    }

    printf("%s", s1);

    return 0;
}