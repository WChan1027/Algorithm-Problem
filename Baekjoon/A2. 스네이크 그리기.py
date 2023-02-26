# https://www.acmicpc.net/contest/problem/956/2
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())

if (n * m) % 2 == 1:
    print(n * m - 1)
    for j in range(1, m+1):
        print(1, j)

    for i in range(2, n+1):
        print(i, m)

    for j in range(m - 1, 0, -1):
        print(n, j)

    i = n-1
    while i > 3:
        if (n - i) % 2 == 1:
            for j in range(1, m):
                print(i, j)
        else:
            for j in range(m-1, 0, -1):
                print(i, j)
        i -= 1

    if j > 3:
        j = m-1
        while j > 1:
            if (m - j) % 2 == 1:
                print(3, j)
                print(2, j)
            else:
                print(2, j)
                print(3, j)
            j -= 1

    print(2, 1)

elif n % 2 == 0:
    print(n * m)
    for j in range(1, m + 1):
        print(1, j)

    for i in range(2, n + 1):
        print(i, m)

    for j in range(m - 1, 0, -1):
        print(n, j)

    i = n - 1
    while i > 1:
        if (n - i) % 2 == 1:
            for j in range(1, m):
                print(i, j)
        else:
            for j in range(m - 1, 0, -1):
                print(i, j)
        i -= 1

else:
    print(n * m)
    for i in range(1, n + 1):
        print(i, 1)

    for j in range(2, m + 1):
        print(n, j)

    for i in range(n - 1, 0, -1):
        print(i, m)

    j = m - 1
    while j > 1:
        if (m - j) % 2 == 1:
            for i in range(1, n):
                print(i, j)
        else:
            for i in range(n - 1, 0, -1):
                print(i, j)
        j -= 1