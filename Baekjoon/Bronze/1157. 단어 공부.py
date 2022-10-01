'''
https://www.acmicpc.net/problem/1157

[문제]

알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
단, 대문자와 소문자를 구분하지 않는다.

'''

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