'''Lv.2 전광판'''

# 문제 : https://softeer.ai/practice/info.do?idx=1&eid=624


# 풀이 1
import sys
input = sys.stdin.readline

# 1. 숫자별 전구 on/off 여부 저장
light = {
    "0" : "1111110",
    "1" : "0110000",
    "2" : "1101101",
    "3" : "1111001",
    "4" : "0110011",
    "5" : "1011011",
    "6" : "1011111",
    "7" : "1110010",
    "8" : "1111111",
    "9" : "1111011",
    " " : "0000000"
}

# 2. T 입력
t = int(input())

# 3. 자연수 A, B 입력 / on/off 전구 비교
result = []
for i in range(t):
    a, b = input().split()
    a = (5 - len(a))*" " + a
    b = (5 - len(b))*" " + b

    cnt = 0
    for digit in range(5):
        for l in range(7):
            if light[a[digit]][l] != light[b[digit]][l]:
                cnt += 1

    result.append(cnt)

# 4. 결과 출력
for r in result:
    print(r)