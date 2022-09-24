import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, num = map(str, input().split())
    print(f'#{test_case}', end=' ')
    for i in num:
        a = '0x' + i
        l = len(format(int(a, 16), 'b'))
        for j in range(4-l):
            print('0', end='')
        print(format(int(a, 16), 'b'), end='')
    print()