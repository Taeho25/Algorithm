// Lv.0 n의 배수

// 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/181937


// 풀이 1
#include <stdio.h>

int solution(int num, int n) {
    return (num % n == 0);
}