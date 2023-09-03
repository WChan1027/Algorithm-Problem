import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

S = input()

Yonsei = ['Y', 'O', 'N', 'S', 'E', 'I']
Korea = ['K', 'O', 'R', 'E', 'A']

for i in S:
    if i == Yonsei[0]:
        Yonsei.pop(0)

    if i == Korea[0]:
        Korea.pop(0)

    if not Yonsei:
        print('YONSEI')
        break

    if not Korea:
        print('KOREA')
        break