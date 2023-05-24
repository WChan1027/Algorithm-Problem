import sys
import itertools
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

# 9명의 선수 (0번 ~ 8번)
players = list(range(9))
# 각 선수의 이닝별 결과
result = [list(map(int, input().split())) for _ in range(N)]

# 0번 선수가 4번 타자가 되는 순서의 조합만 모은 리스트
players_perm = list(p for p in itertools.permutations(players, 9) if p[3] == 0)
answer = 0

# 선수 순서에 따른 점수
def play_baseball(game, player):
    score = 0
    idx = 0

    # 각 이닝
    for inning in game:
        # 아웃카운트 초기화
        out = 0
        # 안타 치는 리스트
        base = []

        # 3 아웃이 될 때까지 진행
        while out < 3:
            if inning[player[idx]] == 0:
                out += 1
            else:
                base.append(inning[player[idx]])

            idx = (idx + 1) % 9

        # 출루한 선수의 수만큼 점수 더하기
        score += len(base)

        # 홈까지 진루하지 못한 선수의 수만큼 점수 빼기
        stay = 0
        for i in base[::-1]:
            stay += i
            if stay < 4:
                score -= 1
            else:
                break

    return score


for case in players_perm:
    answer = max(play_baseball(result, case), answer)

print(answer)