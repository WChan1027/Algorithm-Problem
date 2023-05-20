import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))

if N == 1:
    print('YES')
    print(A[0])
    print(0)
else:
    diff = A[1] - A[0]
    for i in range(N-1):
        if A[i+1] - A[i] != diff:
            print('NO')
            break
    else:
        print('YES')
        print(*A)
        print(*([0]*N))