import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
collect = list(map(int, input().split()))
watch = list(map(int, input().split()))

answer = 0
def spy(n, before, score):
    global answer
    if n == N:
        if score >= M:
            answer += 1
        return

    for i in range(3):
        for j in range(2):
            if j == 0:
                if i == before:
                    spy(n+1, i, score + collect[i]//2)
                else:
                    spy(n+1, i, score + collect[i])
            else:
                if i == before:
                    spy(n+1, i, score + watch[i]//2)
                else:
                    spy(n+1, i, score + watch[i])

spy(0, -1, 0)
print(answer)