class Node:
    def __init__(self, val= None):
        self.val = val
        self.next = None

    def print_data(self):
        node = self
        while node != None:
            print(node.val)
            node = node.next


n1 = Node(37)
n2 = Node(52)
n1.next = n2
n1.print_data()
n0 = Node()
n2.next = n0
n1.print_data()


class DoubleNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


    def print_data(self):
        node = self
        # Forward Traversal
        while node != None:
            print(node.val)
            prevnode = node.prev
            node = node.next


        #Backward Traversal
        #print(prevnode.val)
        prevnode = prevnode.next
        while prevnode!= None:
            print(prevnode.val)
            prevnode = prevnode.prev


n3 = DoubleNode(45)
n4 = DoubleNode(65)
n5 = DoubleNode(75)

n3.next = n4
n4.next = n5
n5.prev = n4
n4.prev = n3

n3.print_data()

