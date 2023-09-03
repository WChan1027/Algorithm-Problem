import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

num = list(map(int, input().split()))
num.sort()

even = -1
odd = -1

for i in range(N-1):
    diff = num[i+1] - num[i]
    if diff % 2:
        if odd == -1 or odd > diff:
            odd = diff


    else:
        if even == -1 or even > diff:
            even = diff

if even == -1:
    for i in range(N-2):
        diff = num[i+2] - num[i]
        if even == -1 or even > diff:
            even = diff

print(even, odd)