import sys



with open('data.txt', 'r', encoding='utf-8') as f:
    #create stacks
    #read in lines
    #determine 

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

for line in moveData:
    move = line.strip().split(' ')

#    print(range(int(move[1])))
    for count in range(int(move[1])):
        #print((move[1]))
        crate = crateStack[int(move[3])-1].pop()
        crateStack[int(move[5])-1].append(crate)
        #print(crateStack[int(move[5])-1], end='')
        #print(crateStack[int(move[3])-1])
#        crateStack[int(move[5])-1].append(crateStack.pop(int(move[3])-1))

stack = 1
print(f'Top crates: ', end='')
for row in crateStack:
    print(f'{stack}:{row.pop()} ', end='')
    stack += 1
print()
#print(stackData)
#print(list(stackMap))
#for stack in stackMap:
#    print(stack[1])
'''
print(f'columns: {stackData.pop()}')
for row in stackData[::-1]:
    for crate in row[1::4]:
        print(crate)




for line in stackData:
    print(line, end='')

'''

