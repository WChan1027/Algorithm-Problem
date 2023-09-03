import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

change = dict()
change['@'] = 'a'
change['['] = 'c'
change['!'] = 'i'
change[';'] = 'j'
change['^'] = 'n'
change['0'] = 'o'
change['7'] = 't'
change[r"\\'"] = 'w'
change[r"\'"] = 'v'

def check(parm):
    cnt = 0
    for key in change.keys():
        if key in parm:
            cnt += parm.count(key)
            parm = parm.replace(key, change[key])

    if cnt >= (len(parm)+1)//2:
        return "I don't understand"

    return parm

for case in range(N):
    word = input().strip()
    print(check(word))