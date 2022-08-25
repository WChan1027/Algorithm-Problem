import sys

sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())

    pw = list(map(int, input().split()))
    rear = -1

    while pw[-1] != 0:
        rear += 1
        decrease = rear % 5 + 1
        a = pw.pop(0)
        if a - decrease <= 0:
            pw.append(0)
        else:
            pw.append(a - decrease)

    print(f'#{tc} {" ".join(map(str, pw))}')