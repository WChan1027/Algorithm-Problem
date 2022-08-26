'''
https://www.acmicpc.net/problem/2669

[문제]

평면에 네 개의 직사각형이 놓여 있는데 그 밑변은 모두 가로축에 평행하다.
이 네 개의 직사각형들은 서로 떨어져 있을 수도 있고, 겹쳐 있을 수도 있고, 하나가 다른 하나를 포함할 수도 있으며, 변이나 꼭짓점이 겹칠 수도 있다.
이 직사각형들이 차지하는 면적을 구하는 프로그램을 작성하시오.

'''
def area(a):
    length = a[2]-a[0]
    height = a[3]-a[1]

    result = length * height

    return result

def overlap_two(a, b):
    overlap_square = [0, 0, 0, 0]

    if a[0] <= b[0] <= a[2]:
        if a[0] <= b[2] <= a[2]:
            overlap_square[0] = b[0]
            overlap_square[2] = b[2]
        else:
            overlap_square[0] = b[0]
            overlap_square[2] = a[2]
    elif a[0] > b[0]:
        if a[0] < b[2] <= a[2]:
            overlap_square[0] = a[0]
            overlap_square[2] = b[2]
        elif a[2] < b[2]:
            overlap_square[0] = a[0]
            overlap_square[2] = a[2]
        else:
            return [0, 0, 0, 0]
    else:
        return [0, 0, 0, 0]

    if a[1] <= b[1] <= a[3]:
        if a[1] <= b[3] <= a[3]:
            overlap_square[1] = b[1]
            overlap_square[3] = b[3]
        else:
            overlap_square[1] = b[1]
            overlap_square[3] = a[3]
    elif a[1] > b[1]:
        if a[1] < b[3] <= a[3]:
            overlap_square[1] = a[1]
            overlap_square[3] = b[3]
        elif a[3] < b[3]:
            overlap_square[1] = a[1]
            overlap_square[3] = a[3]
        else:
            return [0, 0, 0, 0]
    else:
        return [0, 0, 0, 0]

    return overlap_square

def overlap_three(a, b, c):
    return overlap_two(overlap_two(a, b), c)

def overlap_four(a, b, c, d):
    return overlap_two(overlap_three(a, b, c), d)

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))

square_area_one = area(a) + area(b) + area(c) + area(d)
square_area_two = area(overlap_two(a, b)) + area(overlap_two(a, c)) + area(overlap_two(a, d)) + area(overlap_two(b, c)) + area(overlap_two(b, d)) + area(overlap_two(c, d))
square_area_three = area(overlap_three(a, b, c)) + area(overlap_three(a, b, d)) + area(overlap_three(a, c, d)) + area(overlap_three(b, c, d))
square_area_four = area(overlap_four(a, b, c, d))

area_total = square_area_one - square_area_two + square_area_three - square_area_four

print(area_total)