// Lv.0 덧셈식 출력하기

// 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/181947


// 풀이 1
#include <stdio.h>

int main(void) {
    int a;
    int b;
    scanf("%d %d", &a, &b);
    
    printf("%d + %d = %d", a, b, a + b);
    
    return 0;
}