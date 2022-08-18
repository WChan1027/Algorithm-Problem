import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T+1):
    string = input()
    answer = []
    # 문자열을 차례대로 추가하면서 문자가 연속되면 pop으로 제거
    # 결과로 나온 문자열의 길이를 출력
    for i in string:
        answer += [i]
        if len(answer) > 1 and answer[-1] == answer[-2]:
            answer.pop()
            answer.pop()

    print(f'#{test_case} {len(answer)}')