# https://www.acmicpc.net/problem/1157

word = str(input()).upper()

result = {}
for i in word:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1

a = list(result.values())

if a.count(max(a)) > 1:
    answer = '?'
else:
    result = {values: keys for keys, values in result.items()}
    answer = result[max(a)]

print(answer)