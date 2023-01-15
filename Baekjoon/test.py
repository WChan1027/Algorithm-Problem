statue = list(map(int, input().split()))
cnt = 0
answer = 0
for i in range(N):
    if statue[i] == 1:
        cnt += 1
    elif statue[i] == 2:
        if cnt > 0:
            answer += cnt
            cnt = -1
        else:
            cnt -= 1

if cnt > 0:
    answer += cnt

print(answer)