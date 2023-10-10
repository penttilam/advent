import sys


def part1():
    hLocation = (0,0)
    tLocation = (0,0)
    tailMoves = [] 
    with open('data.txt', 'r', encoding='utf-8') as f:
        for line in f:
            direction, movement = line.strip().split(' ')
            movement = int(movement)
            while(movement > 0):
                movement -= 1
                hLocation = move_head(hLocation, direction)
                tLocation = move_tail(hLocation, tLocation)
                tailMoves.append(tLocation)
    print(f'The tail visits {len(set(tailMoves))} locations')



def move_head(location, direction):
    match direction:
        case 'U':
            return (location[0], location[1]+1)
        case 'D':
            return (location[0], location[1]-1)
        case 'L':
            return (location[0]-1, location[1])
        case 'R':
            return (location[0]+1, location[1])

def move_tail(head, tail):
    offset  = (head[0]-tail[0], head[1]-tail[1])
    if abs(offset[0]) == 2:
        if abs(offset[1]) == 1:
            return (tail[0]+(offset[0]/2), tail[1]+offset[1])
        else:
            return (tail[0]+(offset[0]/2), tail[1])
    elif abs(offset[1]) == 2:
        if abs(offset[0]) == 1:
            return (tail[0]+offset[0], tail[1]+(offset[1]/2))
        else:
            return (tail[0], tail[1]+(offset[1]/2))
    else:
        return tail






if __name__ == '__main__':
    part1()

'''
loop
get movement
    loop
    move head
    move tail
'''



