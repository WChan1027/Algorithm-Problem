import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

S = list()
for _ in range(N):
    task = input().split()
    if len(task) == 1:
        if task[0] == 'all':
            S = list(i for i in range(1, 21))
        else:
            S = list()
    else:
        command = task[0]
        num = int(task[1])
        if command == 'add':
            if num not in S:
                S.append(num)
        elif command == 'remove':
            if num in S:
                S.remove(num)
        elif command == 'check':
            if num in S:
                print(1)
            else:
                print(0)
        elif command == 'toggle':
            if num in S:
                S.remove(num)
            else:
                S.append(num)