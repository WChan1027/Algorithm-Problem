import sys

sys.stdin = open('sample_input.txt', encoding='utf-8')

T = int(sys.stdin.readline())

for test_case in range(1, T+1):
    N, M = map(int, sys.stdin.readline().split())
    matrix = []
    answer = ''
    for i in range(N):
        matrix += [list(sys.stdin.readline())]

    # 회문이 1개 있다고 했으므로 while문 사용해서 회문 1개를 찾을 때까지 반복
    while answer == '':
        # 각 행에서 회문 찾기
        for i in range(N):
            for j in range(0, N - M + 1):
                if ''.join(matrix[i][j:j+M-1]) == ''.join(matrix[i][j+M-1:j:-1]):
                    answer = ''.join(matrix[i][j:j+M])

        # 각 열에서 회문 찾기
        # i열의 길이 M인 문자열을 word에 저장하여 회문인지 확인
        for i in range(N):
            for j in range(0, N - M + 1):
                word = ''
                for k in range(M):
                    word += matrix[j+k][i]
                if word == word[::-1]:
                    answer = word


    print(f'#{test_case} {answer}')