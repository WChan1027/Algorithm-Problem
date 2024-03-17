import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())

for test_case in range(T):
    N = int(input())
    students = list(map(str, input().split()))
    answer = float('inf')

    if N > 32:
        answer = 0
    else:
        MBTI = dict()
        for s in students:
            if s in MBTI.keys():
                MBTI[s] += 1
                if MBTI[s] >= 3:
                    answer = 0
                    break
            else:
                MBTI[s] = 1
        else:
            for i in range(N-2):
                for j in range(i+1, N-1):
                    for k in range(j+1, N):
                        result = 0
                        for l in range(4):
                            if students[i][l] != students[j][l]:
                                result += 1
                            if students[i][l] != students[k][l]:
                                result += 1
                            if students[j][l] != students[k][l]:
                                result += 1

                        answer = min(answer, result)

    print(answer)