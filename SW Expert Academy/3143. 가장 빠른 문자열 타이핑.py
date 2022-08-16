T = int(input())

# bruteforce 이용해 패턴의 개수 count

def bruteforce(A, B):
    A_idx, B_idx = 0, 0
    count = 0

    while A_idx < len(A):
        a = A[A_idx]
        b = B[B_idx]

        if a != b:
            A_idx = A_idx - B_idx
            B_idx = -1

        A_idx += 1
        B_idx += 1

        if B_idx == len(B):
            count += 1
            B_idx = 0

    result = len(A) - (len(B)-1)*count
    return result

for test_case in range(1, T+1):
    A, B = input().split()

    result = bruteforce(A, B)
    print(f'#{test_case} {result}')