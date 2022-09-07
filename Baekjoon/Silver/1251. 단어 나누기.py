'''
https://www.acmicpc.net/problem/1251

[문제]

알파벳 소문자로 이루어진 단어를 가지고 아래와 같은 과정을 해 보려고 한다.
먼저 단어에서 임의의 두 부분을 골라서 단어를 쪼갠다.
즉, 주어진 단어를 세 개의 더 작은 단어로 나누는 것이다.
각각은 적어도 길이가 1 이상인 단어여야 한다.
이제 이렇게 나눈 세 개의 작은 단어들을 앞뒤를 뒤집고, 이를 다시 원래의 순서대로 합친다.

예를 들어,

    - 단어 : arrested
    - 세 단어로 나누기 : ar / rest / ed
    - 각각 뒤집기 : ra / tser / de
    - 합치기 : ratserde

단어가 주어지면, 이렇게 만들 수 있는 단어 중에서 사전순으로 가장 앞서는 단어를 출력하는 프로그램을 작성하시오.

'''

word = input()

result = []
a = 0

for i in range(len(word)-2):
    if word[i] < word[a]:
        a = i

b = a+1

for i in range(a+1, len(word)-1):
    if word[i] < word[b]:
        b = i

for i in range(len(word)-2):
    if word[i] == word[a]:
        for j in range(i+1, len(word)-1):
            if word[j] == word[b]:
                result.append("".join([word[i::-1], word[j:i:-1], word[:j:-1]]))

print(sorted(result)[0])
