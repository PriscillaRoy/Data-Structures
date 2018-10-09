
class Stack:
    def __init__(self):
        self.items = [[]]

    def push(self, val):
        min = val
        if(self.items[0] == []):
            self.items[0].append(val)
            self.items[0].append(min)
        elif(self.items[len(self.items) - 1][1] < val):
            min = self.items[len(self.items) - 1][1]
            self.items.append([val, min])
        elif(self.items[len(self.items) - 1][1] > val):
            self.items.append([val, min])


    def pop(self):
        self.items.pop()

    def peek(self):
        return (self.items[len(self.items) - 1])

    def print(self):
        for i in range(0, len(self.items)):
            print(self.items[i])

    def printmin(self):
        print(self.items[len(self.items) - 1][1])


#Testing
s1 = Stack()

s1.push(44)
s1.push(54)
s1.push(32)
s1.push(74)
s1.push(94)
s1.push(21)
s1.push(114)
s1.print()
s1.pop()
s1.print()
s1.printmin()