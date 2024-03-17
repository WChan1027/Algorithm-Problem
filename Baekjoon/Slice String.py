import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
string_separators = list(map(str, input().strip().split()))
M = int(input())
number_separators = list(map(str, input().strip().split()))
K = int(input())
combiners = list(map(str, input().strip().split()))

for combiner in combiners:
    if combiner in string_separators:
        string_separators.remove(combiner)
    elif combiner in number_separators:
        number_separators.remove(combiner)

S = int(input())
standard_string = input().strip().split()

for separator in string_separators:
    result = []
    for string in standard_string:
        result.extend(string.split(separator))
    standard_string = result

for separator in number_separators:
    result = []
    for string in standard_string:
        result.extend(string.split(separator))
    standard_string = result

for string in standard_string:
    if string:
        print(string)