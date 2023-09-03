import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())

for test_case in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    answer = 'Yes'

    a = set()
    b = set()
    before = float('INF')
    for num in nums:
        if num in a:
            if num in b:
                answer = 'No'
                break

        a.add(num)

        if num <= before:
            before = num
        else:
            b.update(i for i in a if i < num)
            before = num

    print(answer)