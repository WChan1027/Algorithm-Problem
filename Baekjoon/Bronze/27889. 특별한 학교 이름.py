import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

school = {'NLCS': 'North London Collegiate School',
          'BHA': 'Branksome Hall Asia',
          'KIS': 'Korea International School',
          'SJA': 'St. Johnsbury Academy'}

name = input().strip()
print(school[name])