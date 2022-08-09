import sys

sys.stdin = open('input.txt')

T = int(sys.stdin.readline())

for test_case in range(1, T+1):
    N = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    num_list = []
    EA = 0
    num = 0

    for i in range(N-1, -1, -1):
        num_list += [a[0]//10**i]
        a[0] = a[0] - (a[0]//10**i * (10**i))

    for i in set(num_list):
        n = 0
        for j in range(N):
            if num_list[j] == i:
                n += 1

        if n == EA:
            if i > num:
                num = i

        elif n > EA:
            EA = n
            num = i

    print(f'#{test_case} {num} {EA}')