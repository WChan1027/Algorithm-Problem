'''
https://www.acmicpc.net/problem/11723

[문제]

비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.

    - add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
    - remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
    - check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
    - toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
    - all: S를 {1, 2, ..., 20} 으로 바꾼다.
    - empty: S를 공집합으로 바꾼다.

'''
import sys

sys.stdin = open('input.txt')
N = int(sys.stdin.readline())

S = set()
for _ in range(N):
    task = sys.stdin.readline().split()
    if len(task) == 1:
        if task[0] == 'all':
            S = set([i for i in range(1, 21)])
        else:
            S = set()
    else:
        command = task[0]
        num = int(task[1])
        if command == 'add':
            if num not in S:
                S.add(num)
        elif command == 'remove':
            if num in S:
                S.discard(num)
        elif command == 'check':
            if num in S:
                print(1)
            else:
                print(0)
        elif command == 'toggle':
            if num in S:
                S.discard(num)
            else:
                S.add(num)