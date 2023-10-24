import sys


def bridge(knots):
    rope = []
    for count in range(knots):
        rope.append(knot())
    rope[0].is_head()
    for x in range(1, knots):
        rope[x].set_leader(rope[x-1])


    with open('data.txt', 'r', encoding='utf-8') as file:
        for line in file:
            direction, movement = line.strip().split(' ')
            movement = int(movement)
            while(movement > 0):
                movement -= 1
                for nots in rope:
                    nots.move(direction)
                '''
                for y in range(20, -20, -1):
                    for x in range(-20, 20):
                        spot = '*'
                        for flot in range(knots):
                            if rope[flot].location == (x,y):
                                spot = str(flot)
                        print(spot, end='')
                    print()
                print('\n\n')
                '''
    print(f'Tail traveled to {rope[knots-1].get_visits()} locations')





class knot:
    def __init__(self):
        self.location = (0,0)
        self.head = False
        self.visited = []
        self.leader = None

    def is_head(self):
        self.head = True

    def set_leader(self, leader):
        self.leader = leader

    def head_move(self, direction):
        match direction:
            case 'U':
                self.location = (self.location[0], self.location[1]+1)
            case 'D':
                self.location = (self.location[0], self.location[1]-1)
            case 'L':
                self.location = (self.location[0]-1, self.location[1])
            case 'R':
                self.location = (self.location[0]+1, self.location[1])

    def follow(self):
        offset  = (self.leader.location[0]-self.location[0], self.leader.location[1]-self.location[1])
        if abs(offset[1]) == 2 and abs(offset[0]) == 2:
            self.location = (self.location[0]+(offset[0]/2), self.location[1]+(offset[1]/2))
        elif abs(offset[0]) == 2:
            if abs(offset[1]) == 1:
                self.location = (self.location[0]+(offset[0]/2), self.location[1]+offset[1])
            else:
                self.location = (self.location[0]+(offset[0]/2), self.location[1])
        elif abs(offset[1]) == 2:
            if abs(offset[0]) == 1:
                self.location = (self.location[0]+offset[0], self.location[1]+(offset[1]/2))
            else:
                self.location = (self.location[0], self.location[1]+(offset[1]/2))
        self.visited.append(self.location)


    def move(self, direction):
        if self.head:
            self.head_move(direction)
        else:
            self.follow()

    def get_visits(self):
        return len(set(self.visited))

if __name__ == '__main__':
#    bridge(2)
    bridge(10)
