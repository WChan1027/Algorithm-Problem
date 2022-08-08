'''
[문제 1]


[문제 설명]

어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다. 
를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. "z"는 1만큼 밀면 "a"가 됩니다. 
문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.


[제한 조건]

공백은 아무리 밀어도 공백입니다.
s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.
s의 길이는 8000이하입니다.
n은 1 이상, 25이하인 자연수입니다.

'''


def solution(s, n):
    answer = ''
    for i in s :
        if ord(i) == 32 :
            answer += i
        elif 65 <= ord(i) <= 90 :
            if (ord(i) + n) > 90 :
                answer += chr((ord(i) + n)%90 + 64)
            else :
                answer += chr((ord(i) + n))
        elif 97 <= ord(i) <= 122 :
            if (ord(i) + n) > 122 : 
                answer += chr((ord(i) + n)%122 + 96)
            else :
                answer += chr((ord(i) + n))
    return answer

'''
[문제 2]

[문제 설명]
정수 배열 numbers가 주어집니다. numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.


[제한사항]
numbers의 길이는 2 이상 100 이하입니다.
numbers의 모든 수는 0 이상 100 이하입니다.
'''


def solution(numbers):
    answer = []
    for i in range(len(numbers)) :
        for j in range(len(numbers)) :
            if i != j :
                answer += [numbers[i] + numbers[j]]
    answer = sorted(list(set(answer)))
    return answer
