# https://www.acmicpc.net/problem/13172
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

M = int(input())

mod = 1000000007


def multiple(result, n):
    if n == 1:
        return result % mod

    if n % 2 == 0:
        half = multiple(result, n // 2)
        return (half * half) % mod

    else:
        return (multiple(result, n - 1) * result) % mod

answer = 0

for _ in range(M):
    N, S = map(int, input().split())

    answer += (S * multiple(N, mod - 2)) % mod

answer %= mod

print(answer)

# answer = 0
# for dice in dices:
#     numerator = dice[1]
#     denominator = dice[0]
#
#     x = 1
#     while True:
#         if (x * mod + 1) % denominator == 0:
#             result = (x * mod + 1) // denominator
#             break
#         else:
#             x += 1
#
#     answer += (numerator * result) % mod
#
# print(answer)




## JS 코드

# let fs = require('fs');
# // let input = fs.readFileSync('/dev/stdin').toString().split('\n');
# let input = require('fs').readFileSync('test.txt').toString().split('\n');
#
# let count = input[0];
# let numbers = [];
#
# for (let i = 1; i < input.length; i++) {
#   if (input[i] !== '') {
#     numbers.push(input[i].split(' '));
#   }
# }
#
# const mod = 1000000007
#
# let answer = 0
#
# for (let i = 0; i < numbers.length; i++) {
#     let numberator = parseInt(numbers[i][1])
#     let denominator = parseInt(numbers[i][0])
#     let x = 1
#     while (true) {
#         if ((x * mod + 1) % denominator == 0) {
#             result = (x * mod +1) / (denominator)
#             break
#         } else {
#             x += 1
#         }
#     }
#     answer += (numberator * result) % mod
# }
#
# console.log(answer)