def reverse_list(node):
    curr = node
    prev = None
    while curr != None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

def build_list(arr):
    head = None
    for el in reversed(arr):
        head = Node(el, head)
    return head

def print_list(node):
    curr = node
    while curr != None:
        print(curr.data)
        curr = curr.next

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

node = build_list(range(10))
r = reverse_list(node)
print_list(r)
