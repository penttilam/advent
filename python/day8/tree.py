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


trees={}
for rowNum, row in enumerate(treeMap):
    for colNum, tree in enumerate(row):
        trees.update({(colNum, rowNum):tree})
        colMx = colNum
    rowMx = rowNum
highScr = 0
for tree in trees:
    #print(f'{tree}, {tree[0]}, {tree[1]}, {trees[tree]}')
    treeH = -1
    viewL = 0
    for x in range(tree[0]-1, -1, -1):
        if trees[(x,tree[1])] < trees[tree]:
            viewL += 1
        else:
            viewL += 1
            break
    viewR = 0
    for x in range(tree[0]+1, rowMx+1, 1):
        if trees[(x,tree[1])] < trees[tree]:
            viewR += 1
        else:
            viewR += 1
            break
    viewH = 0
    for y in range(tree[1]-1, -1, -1):
        if trees[(tree[0], y)] < trees[tree]:
            viewH += 1
        else:
            viewH += 1
            break
    viewB = 0
    for y in range(tree[1]+1, colMx+1, 1):
        if trees[(tree[0],y)] < trees[tree]:
            viewB += 1
        else:
            viewB += 1
            break
    scr = viewL * viewR * viewH * viewB
    if scr > highScr:
        highScr = scr

print(f'The best view has a score of: {highScr}')






