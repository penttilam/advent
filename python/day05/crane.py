import sys

with open('data.txt', 'r', encoding='utf-8') as f:

    stackData = []
    moveData = []
    for line in f:
        if 'move' not in line and line != '\n':
            stackData.append(line)
        elif line == '\n':
            continue
        else:
            moveData.append(line)

crateStack = [[] for stackNum in stackData.pop()[1::4]]
while stackData:
    row = list(stackData.pop()[1::4])
    for pile in crateStack:
        crate = row.pop(0)
        if crate != ' ':
            pile.append(crate)
'''
for line in moveData:
    move = line.strip().split(' ')
    for count in range(int(move[1])):
        crate = crateStack[int(move[3])-1].pop()
        crateStack[int(move[5])-1].append(crate)
'''
for line in moveData:
    crates = []
    move = line.strip().split(' ')
    for count in range(int(move[1])):
        crate = crateStack[int(move[3])-1].pop()
        crates.append(crate)
    for count in range(len(crates)):
        crate = crates.pop() 
        crateStack[int(move[5])-1].append(crate)

stack = 1
print(f'Top crates: ', end='')
for row in crateStack:
    print(f'{stack}:{row.pop()} ', end='')
    stack += 1
print()
