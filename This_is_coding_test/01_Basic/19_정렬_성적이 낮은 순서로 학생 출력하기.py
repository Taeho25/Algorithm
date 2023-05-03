# [19] 정렬 - 성적이 낮은 순서로 학생 출력하기


# 1. N 입력
n = int(input())

# 2. N명의 학생 정보 저장
array = []
for i in range(n):
    input_data = input().split()
    data = (input_data[0], input_data[1])
    array.append(data)

# 3. 정렬 (key: 점수 기준)
array = sorted(array, key=lambda x: x[1])

# 4. 결과 출력
for student in array:
    print(student[0], end=' ')