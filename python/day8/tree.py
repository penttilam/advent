import sys

treeMap = [] 
with open('data.txt', 'r', encoding='utf-8') as f:
    for line in f:
        treeMap.append(line.strip())

visible = set()
for rowNum, row in enumerate(treeMap):
    treeH = -1
    for colNum, tree in enumerate(row):
        if int(tree) > treeH:
            visible.add((colNum,rowNum))
            treeH = int(tree)
    treeH = -1
    for colNum, tree in reversed(list(enumerate(row))):
        if int(tree) > treeH:
            visible.add((colNum,rowNum))
            treeH = int(tree)
for colNum, col in enumerate(zip(*treeMap)):
    treeH = -1
    for rowNum, tree in enumerate(col):
        if int(tree) > treeH:
            visible.add((colNum,rowNum))
            treeH = int(tree)
    treeH = -1
    for rowNum, tree in reversed(list(enumerate(col))):
        if int(tree) > treeH:
            visible.add((colNum,rowNum))
            treeH = int(tree)
print(f'Number of visible trees are: {len(visible)}')
