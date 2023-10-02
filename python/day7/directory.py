import sys


class direct:
    def __init__(self, name):
        self.name = name
        self.parent = None 
        self.directs =[]
        self.files = []
        self.size = 0

    def addFile(self, size, name):
        self.files.append((size, name))
        self.size += size

    def addDirect(self, name):
        name = direct(name)
        name.parent = self
        self.directs.append(name)
        return name

    def getSize(self):
        return self.size

    def getParent(self):
        return self.parent

    def chngDirect(self, dicName):
        for dic in self.directs:
            if dic.name == dicName:
                return dic

    def getSize(self):
        dicSize = 0
        for dic in self.directs:
            dicSize += dic.getSize()
        return dicSize + self.size



current = None
root = direct('root')
directories = [root]
with open('data.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.strip())
        elements = line.strip().split(' ')
        match elements[0]:
            case '$':
                if elements[1] == 'cd':
                    if elements[2]  == '/':
                        current = root
                    elif elements[2] == '..':
                        current = current.getParent()
                    else:
                        current = current.chngDirect(elements[2])
                else:
                    continue
            case 'dir':
                directories.append(current.addDirect(elements[1]))
            case _:
                current.addFile(int(elements[0]), elements[1])
totalSum = 0
for dics in directories:
    size = dics.getSize()
    if size < 100000:
        totalSum += size

print(f'Total Size of directories under 100000 is: {totalSum}')

        
print(f'{root.name}, {root.size}, {[dic.name for dic in root.directs]}, {root.getSize()}')
            

