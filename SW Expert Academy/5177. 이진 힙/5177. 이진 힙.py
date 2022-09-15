import sys
sys.stdin = open('sample_input.txt')


T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    tree = [[0, 0, 0, 0] for _ in range(N+1)]
    value = list(map(int, input().split()))
    value.insert(0, 0)

    # 값 부여
    for i in range(1, N+1):
        if i*2 <= N:
            tree[i][0] = i*2
        if i*2 + 1 <= N:
            tree[i][1] = i*2 + 1
        tree[i][2] = i//2
        tree[i][3] = value[i]

    # 최소 힙
    last = 0
    for i in range(1, len(value)):
        last += 1
        child = last
        parent = child//2

        while parent >= 1 and tree[parent][3] > tree[child][3]:
            tree[parent][3], tree[child][3] = tree[child][3], tree[parent][3]
            child = parent
            parent = parent//2

    # 조상들의 값의 합
    answer = 0
    N = N//2
    while tree[N][3] != 0:
        answer += tree[N][3]
        N = N//2

    print(f'#{test_case} {answer}')