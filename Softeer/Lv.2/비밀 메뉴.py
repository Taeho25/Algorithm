'''Lv.2 비밀 메뉴'''

# 문제 : https://softeer.ai/practice/info.do?idx=1&eid=623


# 풀이 1
import sys
input = sys.stdin.readline

# 1. 입력
m, n, k = map(int, input().split())
secret_n = list(map(str, input().split()))
user_n = list(map(str, input().split()))

# 2. 리스트를 문자열로
secret_n = "".join(secret_n)
user_n = "".join(user_n)

# 3. 레시피 확인
if secret_n in user_n:
    result = 'secret'
else:
    result = 'normal'

print(result)