'''Lv.2 장애물 인식 프로그램'''

# 문제 : https://softeer.ai/practice/info.do?idx=1&eid=409


# 풀이 1
import sys
input = sys.stdin.readline

# 1. 지도 크기 N / N줄에 N개의 자료 입력
N = int(input())
ground = []
for _ in range(N):
    ground.append(list(map(int, input().rstrip())))
#print(ground)

# 3. 장애물 확인 함수
def check_block(x, y):
    global block_cnt
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    else:
        if ground[x][y] == 1:
            ground[x][y] = 0  # 방문체크
            block_cnt += 1  # 한 칸 세기
            check_block(x-1, y) # 상
            check_block(x+1, y) # 하
            check_block(x, y-1) # 좌
            check_block(x, y+1) # 우
            return True
    return False

# 4. 장애물 블록 확인
block = []
for i in range(N):
    for j in range(N):
        block_cnt = 0
        if check_block(i, j) == True:
            block.append(block_cnt)
#print(block)

# 5. 정렬, 결과 출력
block.sort()
print(len(block))
for b in block:
    print(b)