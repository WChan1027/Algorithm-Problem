# https://www.acmicpc.net/problem/17081
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())

dungeon = [list(map(str, input().strip())) for _ in range(N)]
actions = list(map(str, input().strip()))
monsters = dict()
items = dict()

K = 0
L = 0
for i in range(N):
    for j in range(M):
        if dungeon[i][j] == '&' or dungeon[i][j] == 'M':
            K += 1
        elif dungeon[i][j] == 'B':
            L += 1
        elif dungeon[i][j] == '@':
            now = (i, j)

for monster in range(K):
    R, C, S, W, A, H, E = map(str, input().split())
    monsters[f'{R}x{C}'] = [S, W, A, H, E]

for item in range(L):
    R, C, T, S = map(str, input().split())
    items[f'{R}x{C}'] = [T, S]

# 턴 수
T = 0
# 주인공의 상태
Stat = {'Lv': 1, 'HP': 20, 'MaxHP': 20, 'Attack': 0, 'Defence': 0, 'Exp': 0, 'MaxExp': 0, 'Weapon': 0, 'Armor': 0, 'Accessories': {}}

# 주인공이 머무르던 위치가 함정인지 기록하는 변수
isTrap = 0

# 게임이 끝났을 때의 메시지
EndMessage = 'Press any key to continue.'
print(monsters)

## 전투
# stat : 주인공의 상태
# enemy : 몬스터의 정보
def battle(stat, enemy):
    return stat

## 보물상자 열기
# stat : 주인공의 상태
# treasure : 아이템의 정보
def open_treasure(stat, treasure):
    return stat

for action in actions:
    ## 이동
    if action == 'R':
        next = (now[0], now[1] + 1)
        if 0 <= next[1] < M and dungeon[next[0]][next[1]] != '#':
            if isTrap == 0:
                dungeon[now[0]][now[1]] = '.'
            else:
                dungeon[now[0]][now[1]] = '^'
                isTrap = 1
            now = next
    elif action == 'L':
        next = (now[0], now[1] - 1)
        if 0 <= next[1] < M and dungeon[next[0]][next[1]] != '#':
            if isTrap == 0:
                dungeon[now[0]][now[1]] = '.'
            else:
                dungeon[now[0]][now[1]] = '^'
                isTrap = 1
            now = next
    elif action == 'U':
        next = (now[0] - 1, now[1])
        if 0 <= next[0] < M and dungeon[next[0]][next[1]] != '#':
            if isTrap == 0:
                dungeon[now[0]][now[1]] = '.'
            else:
                dungeon[now[0]][now[1]] = '^'
                isTrap = 1
            now = next
    elif action == 'D':
        next = (now[0] + 1, now[1])
        if 0 <= next[0] < M and dungeon[next[0]][next[1]] != '#':
            if isTrap == 0:
                dungeon[now[0]][now[1]] = '.'
            else:
                dungeon[now[0]][now[1]] = '^'
                isTrap = 1
            now = next

    ## 이동한 곳의 정보 확인
    # 빈칸일 때
    if dungeon[now[0]][now[1]] == '.':
        dungeon[now[0]][now[1]] = '@'
    # 몬스터를 만났을 때
    elif dungeon[now[0]][now[1]] == '&':
        # 전투
        battle(Stat, monsters[f'{now[0]+1}x{now[1]+1}'])
        if Stat['HP'] == 0:
            continue
    # 보물상자를 발견했을 때
    elif dungeon[now[0]][now[1]] == 'B':
        dungeon[now[0]][now[1]] = '@'
        continue
    # 함정을 밟았을 때
    elif dungeon[now[0]][now[1]] == '^':
        isTrap = 1
        continue
    # 보스를 만났을 때
    elif dungeon[now[0]][now[1]] == 'M':
        # 전투
        continue



for floor in dungeon:
    print(''.join(floor))

print('Passed Turns :', T)
print('LV :', Stat['Lv'])
print('HP :', Stat['HP'])
print('ATT:', Stat['Attack'])
print('DEF :', Stat['Defence'])
print('EXP :', Stat['Exp'])
print(EndMessage)