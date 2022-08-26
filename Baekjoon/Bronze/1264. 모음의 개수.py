'''
https://www.acmicpc.net/problem/1264

[문제]

영문 문장을 입력받아 모음의 개수를 세는 프로그램을 작성하시오. 
모음은 'a', 'e', 'i', 'o', 'u'이며 대문자 또는 소문자이다.

'''

vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while True:
    test_case = input()
    if test_case == '#':
        break

    n = 0
    for i in test_case:
        if i in vowel:
            n += 1
    
    print(n)