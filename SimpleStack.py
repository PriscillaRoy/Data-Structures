
class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        self.items.pop()

    def peek(self):
        return (self.items[len(self.items) - 1])

    def print(self):
        for i in range(0, len(self.items)):
            print(self.items[i])



s1 = Stack()

s1.push(44)
s1.push(54)
s1.push(64)
s1.push(74)
s1.print()
s1.pop()
s1.print()