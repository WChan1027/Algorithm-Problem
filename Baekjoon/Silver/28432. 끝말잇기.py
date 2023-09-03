import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input().strip())

record = [input().strip() for _ in range(N)]

M = int(input().strip())

candi = [input().strip() for _ in range(M)]

if N == 1 or M == 1:
    answer = candi[0]
elif record[0] == '?':
    for word in candi:
        if word[-1] == record[1][0] and word not in record:
            answer = word
            break
elif record[N-1] == '?':
    for word in candi:
        if word[0] == record[N-2][-1] and word not in record:
            answer = word
            break
else:
    for i in range(1, N-1):
        if record[i] == '?':
            first = record[i-1][-1]
            last = record[i+1][0]
            break
    for word in candi:
        if word[0] == first and word[-1] == last and word not in record:
            answer = word
            break

print(answer)