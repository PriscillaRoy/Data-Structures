class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def in_order(root):

    if root:
        in_order(root.left)
        print(root.val)
        in_order(root.right)

def pre_order(root):

    if root:
        print(root.val)
        pre_order(root.left)
        pre_order(root.right)

def post_order(root):

    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.val)

#Testing
root = Node(4)
n2 = Node(2)
n3 = Node(6)
n4 = Node(1)
n5 = Node(3)
n6 = Node(5)
n7 = Node(7)

root.left = n2
root.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7

in_order(root)
print("#################")
pre_order(root)
print("#################")
post_order(root)

