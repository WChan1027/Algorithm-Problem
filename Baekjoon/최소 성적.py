import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, X = map(float, input().split())

standard_score = X + 0.01

lst = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0}
score = 0
m_sum = 0
for _ in range(int(N)-1):
    m, s = map(str, input().strip().split())
    m_sum += int(m)
    score += float(m) * lst[s]

m = int(input())
m_sum += m

rest = round(round((standard_score) * m_sum, 2) - round(score, 2), 2)
result = round(rest / m, 2)

answer = ''
for case in lst:
    if lst[case] >= result:
        answer = case
    else:
        break

print(answer) if answer else print('impossible')
