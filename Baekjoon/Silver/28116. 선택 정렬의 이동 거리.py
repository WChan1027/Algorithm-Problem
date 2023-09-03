import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))
distance = [0] * N
num_idx = {}
idx = 0
for num in A:
    num_idx[num] = idx
    idx += 1

for i in range(N):
    if num_idx[i+1] != i:
        num_idx[A[i]] = num_idx[i+1]
        distance[A[i]-1] += num_idx[i+1] - i
        distance[i] += num_idx[i+1] - i
        A[num_idx[A[i]]] = A[i]
        A[i] = i+1

print(*distance)