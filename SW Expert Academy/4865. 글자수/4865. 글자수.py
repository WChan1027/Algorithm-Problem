import sys

sys.stdin = open('sample_input.txt', encoding='utf-8')

T = int(sys.stdin.readline())

for test_case in range(1, T+1):
    str1 = sys.stdin.readline()
    str2 = sys.stdin.readline()
    str_num = {}
    answer = 0

    # str1의 문자들을 dict에 {str : 0} 형태로 저장
    for i in str1[:-1]:
        str_num[i] = 0


    # str2의 문자가 str1에 포함되어 있으면 dict에 count
    for i in str2:
        if i in str_num.keys():
            str_num[i] += 1


    # dict의 values에 저장된 숫자들을 리스트로 변환하여 최대값 찾기
    str_count = list(str_num.values())


    for i in range(len(str_count)):
        if str_count[i] > answer:
            answer = str_count[i]

    print(f'#{test_case} {answer}')