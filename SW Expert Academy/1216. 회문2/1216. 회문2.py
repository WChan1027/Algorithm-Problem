import sys

sys.stdin = open('input.txt', encoding='utf-8')


# 길이가 2 또는 3인 회문을 찾아 양쪽으로 길이를 확장시켜 회문의 길이를 구한다.
for test_case in range(10):
    tc = int(sys.stdin.readline())

    matrix = []
    answer = 0

    for i in range(100):
        matrix += [list(map(str, sys.stdin.readline()[0:100]))]

    # 행에서 회문찾기
    for i in range(100):
        for j in range(1, 99):
            if j < 50:
                # 길이가 3인 회문 찾기
                if matrix[i][j-1:j+1] == matrix[i][j+1:j-1:-1]:
                    for k in range(j):
                        if matrix[i][j - k - 1:j + k + 1] == matrix[i][j + k + 1:j - k - 1:-1]:     # k만큼 확장해가며 회문인지 확인
                            if 2 * k + 3 > answer:      # 회문의 길이가 최댓값인지 확인
                                answer = 2*k+3
                        else:
                            break
                # 길이가 2인 회문 찾기
                if matrix[i][j-1:j] == matrix[i][j:j-1:-1]:
                    for k in range(j):
                        if matrix[i][j - k - 1:j + k] == matrix[i][j + k:j - k - 1:-1]:
                            if 2 * k + 2 > answer:
                                answer = 2*k + 2
                        else:
                            break
            else:
                if matrix[i][j-1:j+1] == matrix[i][j+1:j-1:-1]:
                    for k in range(j):
                        if matrix[i][j - k - 1:j + k + 1] == matrix[i][j + k + 1:j - k - 1:-1]:
                            if 2 * k + 3 > answer:
                                answer = 2*k+3
                        else:
                            break
                if matrix[i][j:j + 1] == matrix[i][j + 1:j:-1]:
                    for k in range(j):
                        if matrix[i][j - k:j + k + 1] == matrix[i][j + k + 1:j - k:-1]:
                            if 2 * k + 2 > answer:
                                answer = 2*k + 2
                        else:
                            break
    # 열에서 회문찾기
    for i in range(100):
        for j in range(1, 99):
            word = ''
            if j < 50:
                # 길이가 3인 회문을 찾은 후 확장
                word = matrix[j-1][i] + matrix[j][i] + matrix[j+1][i]
                if word == word[::-1]:
                    word = ''
                    for k in range(j):
                        for l in range(-k-1, k+2):
                            word += matrix[j+l][i]
                        if word == word[::-1]:
                            if 2*k+3 > answer:
                                answer = 2*k+3
                            word = ''
                        else:
                            word = ''
                            break
                # 길이가 4인 회문을 찾은 후 확장
                word = matrix[j-1][i] + matrix[j][i] + matrix[j+1][i] + matrix[j+2][i]
                if word == word[::-1]:
                    word = ''
                    for k in range(j):
                        for l in range(-k-1, k+3):
                            word += matrix[j+l][i]
                        if word == word[::-1]:
                            if 2*k + 4 > answer:
                                answer = 2*k + 4
                            word = ''
                        else:
                            word = ''
                            break


            else:
                word = matrix[j-1][i] + matrix[j][i] + matrix[j+1][i]
                if word == word[::-1]:
                    word = ''
                    for k in range(99 - j):
                        for l in range(-k-1, k+2):
                            word += matrix[j+l][i]
                        if word == word[::-1]:
                            if 2 * k + 3 > answer:
                                answer = 2 * k + 3
                            word = ''
                        else:
                            word = ''
                            break

                word = matrix[j - 2][i] + matrix[j - 1][i] + matrix[j][i] + matrix[j + 1][i]
                if word == word[::-1]:
                    word = ''
                    for k in range(99 - j):
                        for l in range(-k - 2, k + 2):
                            word += matrix[j + l][i]
                        if word == word[::-1]:
                            if 2 * k + 4 > answer:
                                answer = 2 * k + 4
                            word = ''
                        else:
                            word = ''
                            break

    print(f'#{tc} {answer}')