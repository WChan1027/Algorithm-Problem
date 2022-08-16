import sys

sys.stdin = open('sample_input.txt', encoding='utf-8')

T = int(sys.stdin.readline())

for test_case in range(1,T+1):
    tc = sys.stdin.readline()

    answer = 0
    n1 = 0
    n2 = 0

    for i in range(len(tc)):
        if tc[i] == '(':
            if tc[i+1] == ')':
                answer += n2
            else :
                n1 += 1
                n2 += 1
        if tc[i] == ')':
            if tc[i-1] == ')':
                n2 -= 1

    answer += n1

    print(f'#{test_case} {answer}')