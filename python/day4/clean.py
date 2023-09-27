import sys

with open('list.txt', 'r', encoding='utf-8') as f:
    overlaps = 0
    for line in f:
        pair1, pair2 =[cSet.split('-') for cSet in line.strip().split(',')]
        if int(pair1[0]) <= int(pair2[0]) <= int(pair1[1]):
            overlaps += 1
        elif int(pair2[0]) <= int(pair1[0]) <= int(pair2[1]):
            overlaps += 1
print(f'Total Contained Sets: {overlaps}')
