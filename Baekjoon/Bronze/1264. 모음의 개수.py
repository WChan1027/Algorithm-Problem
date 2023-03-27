# https://www.acmicpc.net/problem/1264

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