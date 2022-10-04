import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    paper = list(map(int, input().split()))

    group = [[0]*(N+1) for _ in range(N+1)]
    for i in range(M):
        group[paper[2*i]][paper[2*i+1]] = 1
        group[paper[2*i+1]][paper[2*i]] = 1

    visited = [0] * (N+1)
    answer = 0

    for i in range(1, N+1):
        if visited[i] == 0:     # 아직 조에 들어가지 않았으면
            answer += 1     # 조 +1
            visited[i] = 1      # i가 조에 들어갔음을 표시
            stack = [i]     # i의 조
        while stack:        # i의 조 찾기
            a = stack.pop()
            for i in range(1, N+1):     # 학생들 중에서
                if group[a][i] == 1 and visited[i] == 0:        # i가 신청서로 지목하거나, 지목됐을 때
                    visited[i] = 1      # 조에 들어갔음을 표시
                    stack.append(i)     # stack에 추가하여 신청서 확인

    print(f'#{test_case} {answer}')