# https://www.acmicpc.net/problem/9019
import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())

for test_case in range(T):
    A, B = map(int, input().split())

    que = deque()
    # (변환된 숫자, '지금까지의 명령어') 형태로 que에 저장
    que.append((A, ''))
    # 변환된 적 있는 숫자인지 확인하기 위한 리스트 (0 ~ 9999)
    visited = [0] * 10000

    while que:
        num, answer = que.popleft()

        # 변환된 숫자가 B라면
        if num == B:
            # 명령어 출력
            print(answer)
            break

        # num이 D, S, L, R 명령어에 의해 변환될 수 있는 숫자
        next_num = [(num*2) % 10000, (num-1) % 10000, (num*10 + num//1000) % 10000, (num//10 + (num%10)*1000) % 10000]
        next_register = ['D', 'S', 'L', 'R']

        # D, S, L, R 명령어에 의해 변환된 숫자들에 대해
        for i in range(4):
            # 변환된 적 없으면
            if visited[next_num[i]] == 0:
                # (새로 변환된 숫자, 기존 명령어 + '추가된 명령어')를 que에 추가
                que.append([next_num[i], answer + next_register[i]])
                # 변환된 것을 체크
                visited[next_num[i]] = 1