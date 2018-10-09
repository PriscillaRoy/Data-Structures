class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None

    def print_data(self):
        node = self
        while node != None:
            print(node.val)
            node = node.next


    def reverse_list(self):
        node = self
        head = Node(node.val)
        node = node.next
        while(node != None):
            n = Node(node.val)
            n.next = head
            head = n
            node = node.next
        return head
    def palindrome_check(self, nodeA):
        nodeB = self
        while(nodeA != None and nodeB != None):
            if(nodeA.val != nodeB.val):
                return False
            nodeA = nodeA.next
            nodeB = nodeB.next
        return True


n0 = Node(5)
n1 = Node(6)
n2 = Node(7)
n3 = Node(8)
n0.next = n1
n1.next = n2
n2.next = n3

n0.print_data()

n4 = n0.reverse_list()

n4.print_data()

print("Checking for Palindrome")
if(n4.palindrome_check(n0)):
    print("Yes Palindrome")
else:
    print("Not Palindrome")


n0 = Node(1)
n1 = Node(4)
n2 = Node(4)
n3 = Node(1)
n0.next = n1
n1.next = n2
n2.next = n3

n0.print_data()

n4 = n0.reverse_list()

n4.print_data()

print("Checking for Palindrome")
if(n4.palindrome_check(n0)):
    print("Yes Palindrome")
else:
    print("Not Palindrome")