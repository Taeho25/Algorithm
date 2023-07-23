// Lv.0 홀짝에 따라 다른 값 반환하기

// 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/181935


// 풀이 1
#include <stdio.h>
#include <math.h>

int solution(int n) {
    int answer = 0;
    
    if (n % 2 == 1){
        while(n > 0){
            answer += n;
            n -= 2;
        }
    }
    else{
        while(n > 0){
            answer += pow(n, 2);
            n -= 2;
        }
    }
    
    return answer;
}