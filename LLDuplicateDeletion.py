class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def print_data(self):
        node = self
        while node != None:
            print(node.val)
            node = node.next

    def duplicateDelete(self):
        s = set()
        node = self
        previous = self
        s.add(node.val)
        node = node.next
        while node != None:
            print(s)
            if(node.val in s):
                previous.next = node.next
                print("I'm in IF > ", node.val)
            else:
                s.add(node.val)
                previous = node
            node = node.next



n1 = Node(37)
n2 = Node(52)
n3 = Node(62)
n4 = Node(72)
n5 = Node(8)
n6 = Node(62)
n7 = Node(92)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7

n1.print_data()
n1.duplicateDelete()
print("***********After Duplicate Deletion***************")
n1.print_data()



s1 = set()
s1.add(1)
s1.add(2)
s1.add(3)
s1.add(4)
print(s1)

if( 4 in s1):
    print("Yes")


