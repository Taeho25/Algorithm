// Lv.0 flag에 따라 다른 값 반환하기

// 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/181933


// 풀이 1
#include <stdio.h>
#include <stdbool.h>

int solution(int a, int b, bool flag) {
    if (flag)
        return a+b;
    else
        return a-b;
}