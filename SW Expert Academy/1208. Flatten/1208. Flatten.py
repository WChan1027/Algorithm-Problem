import sys

sys.stdin = open('input.txt')

T = 10

for test_case in range(1, 11):
    N = int(sys.stdin.readline())
    boxes = list(map(int, sys.stdin.readline().split()))

    total = 0
    for height in boxes:
        total += height
    
    average = total // 100
    remainer = total % 100

    difference = 0
    for height in boxes:
        if height > average:
            difference += height - average
        else:
            difference += average - height
    
    dump = (difference - remainer) // 2

    if dump <= N:
        if remainer == 0:
            result = 0
        else:
            result = 1

    else:
        max_height = 101
        min_height = -1
        n_max = 0
        n_min = 0

        while n_max <= N:
            max_height -= 1
            for j in range(100):
                if boxes[j] - max_height >= 0:
                    n_max += 1
            
            
        
        while n_min <= N:
            min_height += 1
            for j in range(100):
                if min_height - boxes[j] >= 0:
                    n_min += 1


        result = max_height - min_height

    print(f'#{test_case} {result}')
