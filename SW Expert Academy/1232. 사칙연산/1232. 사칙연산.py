import sys
sys.stdin = open('input.txt')

def in_order(node):
    if node:        # node = 1 루트에서 시작
        if type(tree[tree[node][0]][3]) == int:     # 좌측 자손이 숫자이면 (계산된 상태면)
            if type(tree[tree[node][1]][3]) == int:     # 우측 자손이 숫자이면 (계산된 상태면)
                if tree[node][3] == '+':        # 기호에 따라 계산
                    tree[node][3] = tree[tree[node][0]][3] + tree[tree[node][1]][3]
                elif tree[node][3] == '-':
                    tree[node][3] = tree[tree[node][0]][3] - tree[tree[node][1]][3]
                elif tree[node][3] == '*':
                    tree[node][3] = tree[tree[node][0]][3] * tree[tree[node][1]][3]
                elif tree[node][3] == '/':
                    tree[node][3] = tree[tree[node][0]][3] // tree[tree[node][1]][3]
            else:       # 우측 자손이 기호이면 (계산되지 않은 상태면)
                in_order(int(tree[node][1]))        # 우측 자손으로
        else:       # 좌측 자손이 기호이면 (계산되지 않은 상태면)
            in_order(int(tree[node][0]))        # 좌측 자손으로


for test_case in range(1, 11):
    N = int(input())

    # tree 생성
    tree = [[0, 0, 0, 0] for _ in range(N+1)]
    for i in range(N):
        case = list(map(str, input().split()))
        if len(case) == 2:
            tree[int(case[0])][3] = int(case[1])
        else:
            tree[int(case[0])][3] = case[1]
            tree[int(case[0])][0] = int(case[2])
            tree[int(case[0])][1] = int(case[3])

    # 루트까지 계산이 완료될 때까지 반복
    while str(tree[1][3]) in '+-*/':
        in_order(1)

    answer = tree[1][3]

    print(f'#{test_case} {answer}')