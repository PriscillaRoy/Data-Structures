class SetOfStacks:
    def __init__(self, t):
        self.items = [ [] for i in range(10) ]

        self.threshold = t
        self.stackIndex = 0


    def push_ele(self, val):
        #print("stack len >>", len(self.items[self.stackIndex]) , "threshold",self.threshold)
        if(len(self.items[self.stackIndex])  >= self.threshold):
            #print("I'm here")
            self.stackIndex = self.stackIndex + 1
        self.items[self.stackIndex].append(val)

    def pop_ele(self):
        self.items[self.stackIndex].pop()
        if(len(self.items[self.stackIndex]) == 0 ):
            self.stackIndex  = self.stackIndex - 1

    def print_stacks(self):
        count = 0
        for stack in self.items:
            if(count == self.stackIndex + 1):
                break
            print(stack)
            count = count+1



ss = SetOfStacks(7)
ss.push_ele(52)
ss.push_ele(62)
ss.push_ele(72)
ss.push_ele(52)
ss.push_ele(62)
ss.push_ele(72)
ss.push_ele(52)
ss.push_ele(62)
ss.push_ele(72)
ss.print_stacks()

