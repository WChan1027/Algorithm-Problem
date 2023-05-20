# https://www.acmicpc.net/problem/2412
import sys
from collections import deque, defaultdict
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, T = map(int, input().split())

# y좌표 = [x좌표, x좌표] 형태로 hold 좌표값 저장
holds = defaultdict(list)
for hold in range(n):
    x, y = map(int, input().split())
    holds[y].append([x, 0])

que = deque()
# (x좌표, y좌표, 이동횟수)
que.append((0, 0, 0))
answer = -1

while que:
    # 현재 x좌표, 현재 y좌표, 이동횟수
    now_x, now_y, cnt = que.popleft()

    # 정상에 도착했으면
    if now_y == T:
        # 이동횟수 기록 후 break
        answer = cnt
        break

    # y좌표 차이 2 이하인 hold 선회
    for next_y in range(now_y -2, now_y +3):
        for hold in holds[next_y]:
            # x좌표 차이가 2 이하이고 이동한 적 없으면
            if abs(hold[0] - now_x) <= 2 and hold[1] == 0:
                # 이동횟수 기록
                hold[1] = cnt + 1
                # que에 추가
                que.append((hold[0], next_y, cnt + 1))

print(answer)