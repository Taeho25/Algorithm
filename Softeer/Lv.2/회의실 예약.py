'''Lv.2 회의실 예약'''

# 문제 : https://softeer.ai/practice/info.do?idx=1&eid=626


# 풀이 1
if(0):
    import sys
    input = sys.stdin.readline

    # 1. N, M 입력
    N, M = map(int, input().split())

    # 2. 회의실 이름 N개 입력
    room = {}
    for _ in range(N):
        name = input().rstrip()
        room[name] = [0]*18

    # 3. 회의실 이름, 시작 시각, 종료 시각 M개 입력
    for i in range(M):
        r, s, t = input().split()
        s, t = int(s), int(t)
        for time in range(s, t):
            room[r][time] = 1
    room = sorted(room.items())

    # 4. 정보 정리
    for i in range(N):
        temp = []
        current = 1
        for j in range(9, 18):
            if current == 1 and room[i][1][j] == 0:
                start = j
                current = 0
            elif current == 0 and room[i][1][j] == 1:
                finish = j
                current = 1
                temp.append([start, finish])
        if current == 0:
            temp.append([start, 18])

        # 출력
        print(f'Room {room[i][0]}:')
        if len(temp) == 0:
            print('Not available')
        else:
            print(f'{len(temp)} available:')
            for j in range(len(temp)):
                print(f'{temp[j][0]:02d}-{temp[j][1]}')
        if i != (N-1):
            print('-----')


# 풀이 2
import sys
input = sys.stdin.readline

# 1. N, M 입력
N, M = map(int, input().split())

# 2. 회의실 이름 N개 입력
room = {}
for _ in range(N):
    name = input().rstrip()
    room[name] = [0]*18+[1]

# 3. 회의실 이름, 시작 시각, 종료 시각 M개 입력
for i in range(M):
    r, s, t = input().split()
    s, t = int(s), int(t)
    for time in range(s, t):
        room[r][time] = 1
room = sorted(room.items())

# 4. 정보 정리
for i in range(N):
    temp = []
    current = 1
    for j in range(9, 19):
        if current == 1 and room[i][1][j] == 0:
            start = j
            current = 0
        elif current == 0 and room[i][1][j] == 1:
            finish = j
            current = 1
            temp.append([start, finish])
    # if current == 0:
    #     temp.append([start, 18])

    # 출력    
    print(f'Room {room[i][0]}:')
    if len(temp) == 0:
        print('Not available')
    else:
        print(f'{len(temp)} available:')
        for j in range(len(temp)):
            print(f'{temp[j][0]:02d}-{temp[j][1]}')
    if i != (N-1):
        print('-----')