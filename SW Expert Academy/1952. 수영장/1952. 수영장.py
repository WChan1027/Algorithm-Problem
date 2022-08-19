import sys

sys.stdin = open('sample_input.txt')

def case(N):
    if 3 <= N and len(memo) <= N:
        memo.append(min(case(N-3) + voucher[2], case(N-3) + price[N-3] + price[N-2] + price[N-1], case(N-2) + price[N-2] + price[N-1], case(N-1) + price[N-1]))

    return memo[N]

T = int(input())

for test_case in range(1, T+1):
    voucher = list(map(int, input().split()))
    plan = list(map(int, input().split()))

    price = []
    result = 0

    for i in plan:
        price += [i * voucher[0]]

    for i in range(len(price)):
        if price[i] > voucher[1]:
            price[i] = voucher[1]

    memo = [0, price[0], price[0] + price[1]]

    case(12)
    result = memo[-1]

    if  result > voucher[3]:
        result = voucher[3]

    print(f'#{test_case} {result}')