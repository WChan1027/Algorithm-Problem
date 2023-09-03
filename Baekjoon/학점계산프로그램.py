import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

S = input().strip()

score = S[0]

total = dict()
total['A+'] = total['A'] = total['B+'] = total['B'] = total['C+'] = total['C'] = total['D+'] = total['D'] = total['F'] = 0

for scores in S[1:]:
    if scores == '+':
        score += '+'
    else:
        total[score] += 1
        score = scores

total[score] += 1

answer = (total['A+'] * 4.5 + total['A'] * 4.0 + total['B+'] * 3.5 + total['B'] * 3.0 + total['C+'] * 2.5 + total['C'] * 2.0 + total['D+'] * 1.5 + total['D'] * 1.0) / sum(total.values())

print(answer)