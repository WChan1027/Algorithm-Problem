import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def is_prime(num):
    for i in range(2, num//2):
        if num % i == 0:
            return False
    return True

T = int(input())
prime = [2, 3, 5]

for n in range(6, 2000):
    if is_prime(n):
        prime.append(n)

for test_case in range(T):
    A, B = map(int, input().split())

    score_kuro, score_siro = 0, 0
    turn = True
    idx = 0
    num = 0
    end = 0
    while end == 0:
        for i in range(A, 0, -1):
            if num+i > B:
                end = 1
                continue
            if num+i in prime:
                next_idx = prime.index(num+i)
                if turn:
                    score_kuro += next_idx - idx + 1
                else:
                    score_siro += next_idx - idx + 1
                num += i
                idx = next_idx + 1
                turn = not turn
                break

        else:
            num += 1
            turn = not turn

    if score_kuro > score_siro:
        print('kuro')

    elif score_kuro < score_siro:
        print('siro')

    else:
        print('draw')

