import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

candies = list(map(int, input().split()))

if not sum(candies) % 2:
    print(sum(candies))
else:
    no = float('INF')
    for i in range(N):
        if candies[i] % 2:
            no = min(no, candies[i])

    print(sum(candies) - no)