import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

def count(N):
    cnt = 0
    for i in range(1, N+1):
        if '50' in str(i):
            cnt += 1
    else:
        if '50' in str(N):
            cnt -= 1

    return cnt

print(N + count(N))