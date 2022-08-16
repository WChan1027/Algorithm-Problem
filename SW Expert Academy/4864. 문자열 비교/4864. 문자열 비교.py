import sys

sys.stdin = open('sample_input.txt', encoding='utf-8')

T = int(sys.stdin.readline())

for test_case in range(1, T+1):
    str1 = sys.stdin.readline()
    str2 = sys.stdin.readline()

    # brute force 사용
    str1_idx, str2_idx = 0, 0
    count = 0

    while str2_idx < len(str2):
        a = str1[str1_idx]
        b = str2[str2_idx]

        if a != b:
            str2_idx = str2_idx - str1_idx
            str1_idx = -1

        str1_idx += 1
        str2_idx += 1

        if str1_idx == len(str1):
            count += 1
            break

    print(f'#{test_case} {count}')