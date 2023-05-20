import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

years = []
names = {}
team1 = ''
team2 = ''

for _ in range(3):
    member = list(map(str, input().split()))
    names[int(member[0])] = member[2][0]
    years.append(int(member[1])%100)

years.sort()
names_sort = list(names.keys())
names_sort.sort(reverse=True)

for year in years:
    team1 += str(year)

for name in names_sort:
    team2 += names[name]

print(team1)
print(team2)