import sys


class register:
    def __init__(self, signalList, value = 1, cycle = 1):
        self.value = value
        self.cycle = cycle
        self.signalPoints = signalList
        self.signalStrength = []

    def noop(self):
        self.signalCheck()
        self.cycle += 1

    def addx(self, x):
        self.signalCheck()
        self.cycle += 1
        self.signalCheck()
        self.cycle += 1
        self.value += int(x)

    def signalCheck(self):
        if self.cycle in self.signalPoints:
            self.signalStrength.append((self.cycle, self.value))


def totalSignalStrength(signalList):
    totalStr = 0
    for cycle, value in signalList:
        totalStr += (cycle * value)
    return totalStr



if __name__ == '__main__':
    signals  = [20, 60, 100, 140, 180, 220]
    x = register(signals)
    with open('data2.txt', 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip() == 'noop':
                x.noop()
            else:
                x.addx(str(line.split(' ')[1]))

#    print(x.signalStrength)
    print(f'Total signal Strength is :{totalSignalStrength(x.signalStrength)}')

        







