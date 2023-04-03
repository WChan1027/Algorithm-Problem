import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

vote = list(map(str, input().strip()))
result = {'U': 0, 'D': 0, 'P': 0, 'C': 0, 'UC': 0, 'DP': 0}
answer = []

for word in vote:
    if word == 'U':
        result['U'] += 1

    elif word == 'C':
        result['U'] += 1
        result['UC'] += 1

    elif word == 'D':
        result['D'] += 1

    elif word == 'P':
        result['D'] += 1
        result['DP'] += 1

if result['U'] * 2 - 1 > result['D']:
    answer.append('U')
if result['D'] > 0:
    answer.append('DP')

print(''.join(answer))