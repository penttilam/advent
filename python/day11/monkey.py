import sys
import operator

from icecream import ic

ops = {
        '+':operator.add,
        '-':operator.sub,
        '*':operator.mul,
        '/':operator.floordiv,
        }


def getMonkeyData():
    with open('data.txt', 'r', encoding='utf-8') as file:
        monkeyData = []
        monkeyBlock = []
        for line in file:
            if line == '\n':
                monkeyData.append(monkeyBlock)
                monkeyBlock = []
            else:
                monkeyBlock.append(line)
        monkeyData.append(monkeyBlock)
    return monkeyData

def setMonkey(infoBlock):
    name = infoBlock[0].strip(':\n').split(' ')[1]
    holding = [item.strip(' \n') for item in infoBlock[1].split(': ')[1].split(' ')]
    operators = infoBlock[2].split('=')[1].strip().split()
    test = infoBlock[3].split('by ')[1].strip()
    trueThrow = infoBlock[4].split('monkey ')[1].strip()
    falseThrow = infoBlock[5].split('monkey ')[1].strip()
    return monkey(name, holding, operators, test, trueThrow, falseThrow)

def monkeyPass(itemVal, monkeyNo):
    for monkey in TROOP:
        if monkey.name == monkeyNo:
            monkey.catch(itemVal)


def monkeyBusiness():
    monk1 = 0
    monk2 = 0
    for monkey in TROOP:
        if monkey.inspections > monk1:
            if monk1 > monk2:
                monk2 = monk1
            monk1 = monkey.inspections
        elif monkey.inspections > monk2:
            monk2 = monkey.inspections
    return monk1 * monk2


class monkey:
    def __init__(self, name, holding, operators, test, trueThrow, falseThrow):
        self.name = name
        self.holding = [int(item.strip(' \n,')) for item in holding]
        self.operators = operators
        self.testVal = int(test)
        self.trueThrow = trueThrow
        self.falseThrow = falseThrow
        self.inHand = None
        self.inspections = 0

    def operation(self):
        if self.operators[0] == 'old':
            var1 = self.inHand 
        else:
            var1 = int(self.operators[0])
        if self.operators[2] == 'old':
            var2 = self.inHand
        else:
            var2 = int(self.operators[2])
        self.inHand =  ops[self.operators[1]](var1, var2)
        self.inspections += 1

    def bored(self):
        self.inHand = self.inHand // 3


    def test(self):
        return self.inHand % self.testVal == 0

    def throw(self):
        if self.test():
            monkeyPass(self.inHand, self.trueThrow)
        else:
            monkeyPass(self.inHand, self.falseThrow)

    def catch(self, item):
        self.holding.append(item)

    def turn(self, remainder):
        while self.holding:
            self.inHand = self.holding.pop(0) % remainder
            self.operation()
            #self.bored()
            self.throw()


if __name__ == '__main__':
    TROOP =[]
    rounds = 10000
    for block in getMonkeyData():
        TROOP.append(setMonkey(block))
    chRemain = 1
    for monkey in TROOP:
        chRemain *= monkey.testVal
    while rounds > 0:
        for members in TROOP:
            members.turn(chRemain)
        rounds -= 1
    for monkey in TROOP:
        print(f'Monkey {monkey.name} inspected items {monkey.inspections} times.')
    print(f'Monkey Business is {monkeyBusiness()}')

