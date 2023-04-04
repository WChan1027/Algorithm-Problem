import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

password = input()

key = ord(password[1]) - ord(password[0])
key2 = ord(password[2]) - ord(password[1])

if key == 1 or key == -25:
    if key2 == -10 or key2 == 16:
        print('SJA')
    else:
        print('NLCS')
elif key == 16 or key == -10:
    print('BHA')
elif key == 4 or key == -22:
    print('KIS')