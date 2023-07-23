// Lv.0 공배수

// 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/181936


// 풀이 1
#include <stdio.h>

int solution(int number, int n, int m) {
    return (number % n == 0) && (number % m == 0);
}