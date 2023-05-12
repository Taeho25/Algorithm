'''Lv.2 8단 변속기'''

# 문제 : https://softeer.ai/practice/info.do?idx=1&eid=408


# 풀이 1
trans = map(int, input().split())

if trans[0] == 1:
    ans = 'ascending'
    for i in range(1, 8):
        if trans[i] != (i+1):
            ans = 'mixed'
            break
elif trans[0] == 8:
    ans = 'descending'
    for i in range(1, 8):
        if trans[i] != (8-i):
            ans = 'mixed'
            break
else:
    ans = 'mixed'

print(ans)


# 풀이 2
trans = "".join(input().split())

if trans == "12345678":
    print("ascending")
elif trans == "87654321":
    print("descending")
else:
    print("mixed")