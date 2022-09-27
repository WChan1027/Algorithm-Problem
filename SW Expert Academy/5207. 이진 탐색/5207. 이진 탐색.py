import sys
sys.stdin = open('sample_input.txt')

T = int(input())

# arr : 찾는 리스트, low : 찾는 범위의 왼쪽 값, high : 찾는 범위의 오른쪽 값, key : 찾는 수, direction : 방향
# direction 0 : 왼쪽, direction 1 : 오른쪽
# 문제의 조건을 만족하지 못하면 0을 return, 만족하면 1을 return
def binary_search(arr, low, high, key, direction):
    if low > high:      # 끝까지 찾았을 때 key 가 없으면
        return 0

    else:
        mid = (low + high) // 2     # 중간 지점 지정

        # 중간 지점 값이 key 이면 종료
        if key == arr[mid]:
            return 1

        # 중간 지점 값이 key 보다 크면 왼쪽 조사
        elif key < arr[mid]:
            if direction == 0:      # 바로 전에 왼쪽을 조사 했으면
                return 0
            else:       # 아니라면 왼쪽을 조사
                return binary_search(arr, low, mid-1, key, 0)

        # 중간 지점 값이 key 보다 크면 오른쪽 조사
        else:
            if direction == 1:      # 바로 전에 오른쪽을 조사 했으면
                return 0
            else:       # 아니라면 오른쪽을 조사
                return binary_search(arr, mid+1, high, key, 1)

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    answer = 0

    # B 리스트의 요소들에 대해 순회
    for i in B:
        answer += binary_search(A, 0, N-1, i, -1)       # 처음 방향은 왼쪽(0), 오른쪽(1)이 아닌 수

    print(f'#{test_case} {answer}')