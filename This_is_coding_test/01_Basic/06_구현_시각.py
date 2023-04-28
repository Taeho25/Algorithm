# [06] 구현 - 시각


# 1. H 입력
h = int(input())

# 2. 알고리즘
count = 0
for hh in range(h + 1):    # 0시부터 h시까지 확인
  for mm in range(60):    # 60분 확인
    for ss in range(60):    # 60초 확인
      if '3' in (str(hh) + str(mm) + str(ss)):    # 문자열 hhmmss 안에 '3'이 있으면 +1
        count += 1

# 3. 결과 출력
print(count)