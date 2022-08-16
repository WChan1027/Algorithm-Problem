'''import sys

sys.stdin = open('input.txt', encoding='utf-8')

def sell_point(price, profit):
    point = 0

    for i in range(1, len(price)):
        if price[i] > price[point]:
            point = i

    if point == 0:
        if sorted(price) == price[::-1]:
            return profit

    for i in range(point):
        profit += price[point] - price[i]

    price = price[point+1:]

    return sell_point(price, profit)


T = int(sys.stdin.readline())

for test_case in range(1, T+1):
    N = int(sys.stdin.readline())
    price = list(map(int, sys.stdin.readline().split()))

    profit = 0

    result = sell_point(price, profit)

    print(f'#{test_case} {result}')'''




'''import sys

sys.stdin = open('input.txt', encoding='utf-8')


T = int(sys.stdin.readline())

for test_case in range(1, T+1):
    N = int(sys.stdin.readline())
    price = list(map(int, sys.stdin.readline().split()))

    profit = 0
    finish = 0

    while finish == 0:
        point = 0
        n = len(price)
        for i in range(1, n):
            if price[i] > price[point]:
                point = i

        if point == 0:
            if sorted(price) == price[::-1]:
                finish = 1

        for i in range(point):
            profit += price[point] - price[i]

        price = price[point+1:]

    print(f'#{test_case} {profit}')'''