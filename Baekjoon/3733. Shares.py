'''
https://www.acmicpc.net/problem/3733

[문제]

A group of N persons and the ACM Chief Judge share equally a number of S shares (not necessary all of them).
Let x be the number of shares aquired by each person (x must be an integer). The problem is to compute the maximum value of x.

'''

while True:
    try:
        N, S = map(int, input().split())

        x = S // (N+1)

        print(x)
    except:
        break