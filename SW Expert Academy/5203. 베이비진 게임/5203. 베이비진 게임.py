import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T+1):
    card = list(map(int, input().split()))

    A = []
    B = []
    answer = 0

    for i in range(len(card)):
        if i % 2 == 0:
            A.append(card[i])
            if len(A) >= 3:
                # 같은 숫자 카드 3장이 있으면 승리
                if A.count(card[i]) == 3:
                    answer = 1
                    break
                # 연속된 카드 3장이 있으면 승리
                if card[i] - 1 in A:
                    if card[i] - 2 in A or card[i] + 1 in A:
                        answer = 1
                        break
                elif card[i] + 1 in A:
                    if card[i] + 2 in A:
                        answer = 1
                        break
        else:
            B.append(card[i])
            if len(B) >= 3:
                # 같은 숫자 카드 3장이 있으면 승리
                if B.count(card[i]) == 3:
                    answer = 2
                    break
                # 연속된 카드 3장이 있으면 승리
                if card[i] - 1 in B:
                    if card[i] - 2 in B or card[i] + 1 in B:
                        answer = 2
                        break
                elif card[i] + 1 in B:
                    if card[i] + 2 in B:
                        answer = 2
                        break

    print(f'#{test_case} {answer}')