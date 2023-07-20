// Lv.0 홀짝 구분하기

// 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/181944


// 풀이 1
#include <stdio.h>

int main(void) {
    int a;
    scanf("%d", &a);
    
    if (a % 2 == 0) printf("%d is even", a);
    else printf("%d is odd", a);

    return 0;
}