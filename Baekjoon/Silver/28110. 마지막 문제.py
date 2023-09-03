import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

level = list(map(int, input().split()))
level.sort()

problem = 0
diff = 0
for i in range(N-1):
    if (level[i+1] - level[i])//2 > diff//2:
        diff = level[i+1] - level[i]
        problem = level[i]

if diff < 2:
    print(-1)
else:
    print(problem + diff//2)