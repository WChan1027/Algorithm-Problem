# https://www.acmicpc.net/problem/16198
import sys
import copy
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
W = list(map(int, input().split()))

# N이 최대 10으로, 경우의 수는 최대 8! = 40320가지
# 모든 경우를 완전탐색해도 시간이 오래 걸리지 않음


# 주어진 조건을 반복하는 함수
# energy : 지금까지 모인 에너지
# W : 남은 구슬들의 무게 list
def collect_energy(energy, W):
    global answer
    # 반복이 끝나면 answer과 크기 비교
    if len(W) == 2:
        answer = max(answer, energy)
        return

    # 첫 번째와 두 번째 구슬을 제외한 구슬을 하나씩 선택하여 조건 시행
    for i in range(1, len(W)-1):
        # W를 깊은 복사 하여 사용
        new_W = copy.deepcopy(W)
        # 에너지 더하기
        new_energy = energy + W[i-1] * W[i+1]
        # 선택된 구슬 제거
        del new_W[i]
        # 다음 반복 시행
        collect_energy(new_energy, new_W)

answer = 0
collect_energy(0, W)
print(answer)