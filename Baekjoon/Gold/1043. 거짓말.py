# https://www.acmicpc.net/problem/1043
import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())

know = list(map(int, sys.stdin.readline().split()))
if len(know) > 1:
    know = set(know[1:])
else:
    know = set()

party_people = []
for _ in range(M):
    party_people.append(list(map(int, sys.stdin.readline().split())))


for i in range(len(party_people)):
    if len(party_people[i]) > 1:
        party_people[i] = set(party_people[i][1:])
    else:
        party_people[i] = set(party_people[i])

count = 1
while count != 0:
    count = 0
    i = 0
    while i < len(party_people):
        if know & party_people[i]:
            know = know | party_people[i]
            party_people.remove(party_people[i])
            count += 1
        else:
            i += 1

answer = len(party_people)
print(answer)