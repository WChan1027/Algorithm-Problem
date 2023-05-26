import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T, W = map(int, input().split())

tree = list(int(input())-1 for _ in range(T))

# 가지치기
# check[i][j] = i초가 지나고, j만큼 이동횟수를 소모했을 때의 최댓값
check = [[-1] * T for _ in range(W)]

answer = 0

def plum(time, num, move, total):
    global answer
    # 이동횟수를 모두 소모했을 때
    if move == W:
        total += tree[time:].count(num)
        answer = max(answer, total)
        return

    # 자두가 모두 떨어졌을 때
    if time == T:
        answer = max(answer, total)
        return

    # 가지치기
    if check[move][time] < total:
        check[move][time] = total
    else:
        return

    # 0 : 제자리, 1 : 이동
    for i in range(2):
        if tree[time] == (num+i)%2:
            plum(time+1, (num+i)%2, move + i, total + 1)
        else:
            plum(time+1, (num+i)%2, move + i, total)

    return

plum(0, 0, 0, 0)

print(answer)