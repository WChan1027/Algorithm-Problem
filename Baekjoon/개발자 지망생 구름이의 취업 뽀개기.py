import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

nums = list(map(int, input().split()))

times = [[] for _ in range(5)]

answer = 240

for problem in range(N):
    k, t = map(int, input().split())

    times[k-1].append(t)

for i in range(5):
    times[i].sort()

for i in range(5):
    num = nums[i]
    answer += sum(times[i][1:num])
    answer += times[i][num-1]

print(answer)