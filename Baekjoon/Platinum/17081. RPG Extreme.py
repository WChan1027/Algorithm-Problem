# https://www.acmicpc.net/problem/17081
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

### 게임 초기 상태 설정

## 던전 크기 설정
N, M = map(int, input().split())


## 던전 생성
dungeon = [list(map(str, input().strip())) for _ in range(N)]


## 커맨드 입력
actions = list(map(str, input().strip()))


## 몬스터
monsters = dict()


## 아이템 상자
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
            start = (i, j)          # 시작 위치 기록
            now = (i, j)            # 현재 위치 기록

## 몬스터 생성
for monster in range(K):
    R, C, S, W, A, H, E = map(str, input().split())
    monsters[f'{R}x{C}'] = {'Name': S, 'Attack': int(W), 'Defence': int(A), 'MaxHP': int(H), 'HP': int(H), 'Exp': int(E)}


## 아이템 박스 생성
for item in range(L):
    R, C, T, S = map(str, input().split())
    items[f'{R}x{C}'] = {'Type': T, 'Effect': S}


## 초기 상태
Turn = 0       # 턴 수
Stat = {'Lv': 1, 'HP': 20, 'MaxHP': 20, 'Attack': 2, 'Defence': 2, 'Exp': 0, 'MaxExp': 5, 'Weapon': 0, 'Armor': 0, 'Accessories': []}       # 주인공의 상태
isTrap = 0      # 주인공이 머무르던 위치가 함정인지 기록하는 변수
EndMessage = 'Press any key to continue.'       # 게임이 끝났을 때의 메시지


## 전투
def battle(stat, enemy):        # stat : 주인공 정보, enemy : 몬스터 정보
    enemy = first_attack(stat, enemy)                                                   # 첫 공격
    if enemy['HP'] <= 0:                                                                # 쓰러뜨렸을 때
        stat = victory(stat, enemy)
        return stat
    stat['HP'] -= max(1, enemy['Attack'] - stat['Defence'] - stat['Armor'])             # 방어

    while stat['HP'] > 0 and enemy['HP'] > 0:
        enemy['HP'] -= max(1, stat['Attack'] + stat['Weapon'] - enemy['Defence'])       # 공격
        if enemy['HP'] <= 0:                                                            # 쓰러뜨렸을 때
            stat = victory(stat, enemy)
            return stat
        stat['HP'] -= max(1, enemy['Attack'] - stat['Defence'] - stat['Armor'])         # 방어

    return stat


## 보스 전투
def boss_battle(stat, enemy):
    if 'HU' in stat['Accessories']:                                                     # Hunter 아이템 소유 시
        stat['HP'] = stat['MaxHP']                                                      # 체력 회복

    enemy = first_attack(stat, enemy)                                                   # 첫 공격
    if enemy['HP'] <= 0:                                                                # 쓰러뜨렸을 때
        stat = victory(stat, enemy)
        return stat

    if 'HU' in stat['Accessories']:                                                     # Hunter 아이템 소유 시
        stat['HP'] -= 0                                                                 # 첫 데미지 무시
    else:                                                                               # Hunter 아이템 미소유 시
        stat['HP'] -= max(1, enemy['Attack'] - stat['Defence'] - stat['Armor'])         # 방어

    while stat['HP'] > 0 and enemy['HP'] > 0:
        enemy['HP'] -= max(1, stat['Attack'] + stat['Weapon'] - enemy['Defence'])       # 공격
        if enemy['HP'] <= 0:                                                            # 쓰러뜨렸을 때
            stat = victory(stat, enemy)
            return stat
        stat['HP'] -= max(1, enemy['Attack'] - stat['Defence'] - stat['Armor'])         # 방어

    return stat


## 첫 공격
def first_attack(stat, enemy):
    if 'CO' in stat['Accessories']:                                                             # Courage 아이템 소유 시
        if 'DX' in stat['Accessories']:                                                         # Dexterity 아이템 소유 시
            enemy['HP'] -= max(1, 3 * (stat['Attack'] + stat['Weapon']) - enemy['Defence'])     # 공격력 3배 적용
        else:
            enemy['HP'] -= max(1, 2 * (stat['Attack'] + stat['Weapon']) - enemy['Defence'])     # 공격력 2배 적용
    else:
        enemy['HP'] -= max(1, stat['Attack'] + stat['Weapon'] - enemy['Defence'])               # 공격력 1배 적용

    return enemy


## 승리
def victory(stat, enemy):       # stat : 주인공 정보, enemy : 몬스터 정보
    if 'HR' in stat['Accessories']:                     # HP Regeneration 아이템 소유 시
        stat['HP'] += 3                                 # 체력 3 회복
        if stat['HP'] > stat['MaxHP']:                  # 최대 HP 까지만 회복
            stat['HP'] = stat['MaxHP']

    if 'EX' in stat['Accessories']:                     # Experience 아이템 소유 시
        stat['Exp'] += int(enemy['Exp'] * (1.2))        # 경험치 획득
    else:
        stat['Exp'] += enemy['Exp']

    if stat['Exp'] >= stat['MaxExp']:                   # 레벨 업
        stat = level_up(stat)

    return stat


## 레벨 업
def level_up(stat):     # stat : 주인공 정보
    stat['Lv'] += 1                     # 레벨 1 증가
    stat['MaxHP'] += 5                  # 최대 체력 5 증가
    stat['Attack'] += 2                 # 공격력 2 증가
    stat['Defence'] += 2                # 방어력 2 증가
    stat['HP'] = stat['MaxHP']          # 최대 체력만큼 체력 회복
    stat['MaxExp'] = stat['Lv'] * 5     # 경험치량 갱신
    stat['Exp'] = 0                     # 경험치 0으로 초기화

    return stat

## 아이템 상자 열기
def open_box(stat, item):       # stat : 주인공 정보, item : 아이템 정보
    if item['Type'] == 'W':                                 # 무기가 들어있을 경우
        stat['Weapon'] = int(item['Effect'])                # 무기 장착
    elif item['Type'] == 'A':                               # 방어구가 들어있을 경우
        stat['Armor'] = int(item['Effect'])                 # 방어구 장착
    elif item['Type'] == 'O':                               # 장신구가 들어있을 경우
        if len(stat['Accessories']) < 4:                    # 착용한 장신구가 4개가 안될 때
            if item['Effect'] == 'HR':                      # HR Regeneration이 들어있을 경우
                if 'HR' not in stat['Accessories']:         # HP Regeneration이 없을 때
                    stat['Accessories'].append('HR')        # HP Regeneration 장착
            elif item['Effect'] == 'RE':                    # Reincarnation이 들어있을 경우
                if 'RE' not in stat['Accessories']:         # Reincarnation이 없을 때
                    stat['Accessories'].append('RE')        # Reincarnation 장착
            elif item['Effect'] == 'CO':                    # Courage가 들어 있을 경우
                if 'CO' not in stat['Accessories']:         # Courage가 없을 때
                    stat['Accessories'].append('CO')        # Courage 장착
            elif item['Effect'] == 'EX':                    # Experience가 들어 있을 경우
                if 'EX' not in stat['Accessories']:         # Experience가 없을 때
                    stat['Accessories'].append('EX')        # Experience 장착
            elif item['Effect'] == 'DX':                    # Dexterity가 들어 있을 경우
                if 'DX' not in stat['Accessories']:         # Dexterity가 없을 때
                    stat['Accessories'].append('DX')        # Dexterity 장착
            elif item['Effect'] == 'HU':                    # Hunter가 들어 있을 경우
                if 'HU' not in stat['Accessories']:         # Hunter가 없을 때
                    stat['Accessories'].append('HU')        # Hunter 장착
            elif item['Effect'] == 'CU':                    # Cursed가 들어 있을 경우
                if 'CU' not in stat['Accessories']:         # Cursed가 없을 때
                    stat['Accessories'].append('CU')        # Cursed 장착

    return stat


for action in actions:
    ## 이동
    if action == 'R':                                                   # 오른쪽으로 이동
        next = (now[0], now[1] + 1)
        if 0 <= next[1] < M and dungeon[next[0]][next[1]] != '#':
            if isTrap == 0:
                dungeon[now[0]][now[1]] = '.'
            else:
                dungeon[now[0]][now[1]] = '^'
                isTrap = 1
            now = next
    elif action == 'L':                                                 # 왼쪽으로 이동
        next = (now[0], now[1] - 1)
        if 0 <= next[1] < M and dungeon[next[0]][next[1]] != '#':
            if isTrap == 0:
                dungeon[now[0]][now[1]] = '.'
            else:
                dungeon[now[0]][now[1]] = '^'
                isTrap = 1
            now = next
    elif action == 'U':                                                 # 위로 이동
        next = (now[0] - 1, now[1])
        if 0 <= next[0] < N and dungeon[next[0]][next[1]] != '#':
            if isTrap == 0:
                dungeon[now[0]][now[1]] = '.'
            else:
                dungeon[now[0]][now[1]] = '^'
                isTrap = 1
            now = next
    elif action == 'D':                                                 # 아래로 이동
        next = (now[0] + 1, now[1])
        if 0 <= next[0] < N and dungeon[next[0]][next[1]] != '#':
            if isTrap == 0:
                dungeon[now[0]][now[1]] = '.'
            else:
                dungeon[now[0]][now[1]] = '^'
                isTrap = 1
            now = next
    Turn += 1

    ## 이동한 곳의 정보 확인

    # 빈칸일 때
    if dungeon[now[0]][now[1]] == '.':
        isTrap = 0                          # 함정이 아닌 것을 기록
        dungeon[now[0]][now[1]] = '@'       # 해당 위치로 이동

    # 몬스터를 만났을 때
    elif dungeon[now[0]][now[1]] == '&':
        isTrap = 0                                                  # 함정이 아닌 것을 기록
        Stat = battle(Stat, monsters[f'{now[0]+1}x{now[1]+1}'])     # 전투

        if Stat['HP'] <= 0:                                         # 패배했을 때
            if 'RE' in Stat['Accessories']:                         # Reincarnation 아이템 소유 시
                Stat['Accessories'].remove('RE')                    # Reincarnation 아이템 소모
                Stat['HP'] = Stat['MaxHP']                          # 주인공 체력 회복
                now = start                                         # 시작 위치로 이동
                dungeon[now[0]][now[1]] = '@'                       # 주인공 위치 표시

            else:                                                   # Reincarnation 아이템 미소유 시
                Stat['HP'] = 0                                      # 체력 0
                EndMessage = f"YOU HAVE BEEN KILLED BY {monsters[f'{now[0]+1}x{now[1]+1}']['Name']}.."        # 패배 메시지
                break                                               # 게임 종료

        else:                                                       # 승리했을 때
            dungeon[now[0]][now[1]] = '@'                           # 몬스터가 있던 위치로 이동

    # 아이템 상자를 발견했을 때
    elif dungeon[now[0]][now[1]] == 'B':
        isTrap = 0                          # 함정이 아닌 것을 기록
        Stat = open_box(Stat, items[f'{now[0]+1}x{now[1]+1}'])
        dungeon[now[0]][now[1]] = '@'       # 아이템 상자가 있던 위치로 이동

    # 함정을 밟았을 때
    elif dungeon[now[0]][now[1]] == '^':
        isTrap = 1                                                  # 함정을 밟은 것을 기록

        if 'DX' in Stat['Accessories']:                             # Dexterity 아이템 소유 시
            Stat['HP'] -= 1                                         # 체력 1 감소
        else:                                                       # Dexterity 아이템 미소유 시
            Stat['HP'] -= 5                                         # 체력 5 감소

        if Stat['HP'] <= 0:                                         # 사망했을 때
            if 'RE' in Stat['Accessories']:                         # Reincarnation 아이템 소유 시
                Stat['Accessories'].remove('RE')                    # Reincarnation 아이템 소모
                Stat['HP'] = Stat['MaxHP']                          # 주인공 체력 회복
                now = start                                         # 시작 위치로 이동
                dungeon[now[0]][now[1]] = '@'                       # 주인공 위치 표시
                isTrap = 0                                          # 함정이 아닌 것을 기록

            else:                                                   # Reincarnation 아이템 미소유 시
                Stat['HP'] = 0                                      # 체력 0
                EndMessage = "YOU HAVE BEEN KILLED BY SPIKE TRAP.."  # 패배 메시지
                break                                               # 게임 종료
        else:
            dungeon[now[0]][now[1]] = '@'                           # 해당 위치로 이동

    # 제자리에 머무를 때
    elif dungeon[now[0]][now[1]] == '@':
        if isTrap == 1:                                             # 현재 위치가 함정일 경우
            if 'DX' in Stat['Accessories']:                         # Dexterity 아이템 소유 시
                Stat['HP'] -= 1                                     # 체력 1 감소
            else:                                                   # Dexterity 아이템 미소유 시
                Stat['HP'] -= 5                                     # 체력 5 감소

            if Stat['HP'] <= 0:                                     # 사망했을 때
                if 'RE' in Stat['Accessories']:                     # Reincarnation 아이템 소유 시
                    Stat['Accessories'].remove('RE')                # Reincarnation 아이템 소모
                    Stat['HP'] = Stat['MaxHP']                      # 주인공 체력 회복
                    dungeon[now[0]][now[1]] = '^'                   # 함정 위치 표시
                    now = start                                     # 시작 위치로 이동
                    dungeon[now[0]][now[1]] = '@'                   # 주인공 위치 표시
                    isTrap = 0                                      # 함정이 아닌 것을 기록

                else:                                               # Reincarnation 아이템 미소유 시
                    dungeon[now[0]][now[1]] = '^'                   # 함정 위치 표시
                    Stat['HP'] = 0                                  # 체력 0
                    EndMessage = "YOU HAVE BEEN KILLED BY SPIKE TRAP.."  # 패배 메시지
                    break                                           # 게임 종료

    # 보스를 만났을 때
    elif dungeon[now[0]][now[1]] == 'M':
        isTrap = 0                                                  # 함정이 아닌 것을 기록
        Stat = boss_battle(Stat, monsters[f'{now[0]+1}x{now[1]+1}'])     # 전투

        if Stat['HP'] <= 0:                                         # 패배했을 때
            if 'RE' in Stat['Accessories']:                         # Reincarnation 아이템 소유 시
                Stat['Accessories'].remove('RE')                    # Reincarnation 아이템 소모
                Stat['HP'] = Stat['MaxHP']                          # 주인공 체력 회복
                now = start                                         # 시작 위치로 이동
                dungeon[now[0]][now[1]] = '@'                       # 주인공 위치 표시

            else:                                                   # Reincarnation 아이템 미소유 시
                Stat['HP'] = 0                                      # 체력 0
                EndMessage = f"YOU HAVE BEEN KILLED BY {monsters[f'{now[0]+1}x{now[1]+1}']['Name']}.."
                break                                               # 게임 종료

        else:                                                       # 승리했을 때
            dungeon[now[0]][now[1]] = '@'                           # 몬스터가 있던 위치로 이동
            EndMessage = 'YOU WIN!'                                 # 승리 메시지
            break                                                   # 게임 종료

for floor in dungeon:
    print(''.join(floor))
print(f"Passed Turns : {Turn}")
print(f"LV : {Stat['Lv']}")
print(f"HP : {Stat['HP']}/{Stat['MaxHP']}")
print(f"ATT : {Stat['Attack']}+{Stat['Weapon']}")
print(f"DEF : {Stat['Defence']}+{Stat['Armor']}")
print(f"EXP : {Stat['Exp']}/{Stat['MaxExp']}")
print(EndMessage)