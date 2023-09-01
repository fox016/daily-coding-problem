"""
Add two numbers represented by linked lists
e.g. 947 represented as 7 -> 4 -> 9
"""

def add_lists(n1, n2, carry=0):
    if n1 == None and n2 == None and carry == 0:
        return None
    v1 = n1.data if n1 else 0
    v2 = n2.data if n2 else 0
    val = v1 + v2 + carry
    carry = 0
    if val >= 10:
        val, carry = (val-10, 1)
    return Node(val, add_lists(n1.next if n1 else None, n2.next if n2 else None, carry))

"""
def add_lists(l1, l2):
    n1, n2, sum_list, carry = l1, l2, None, 0
    while True:
        if n1 == None and n2 == None:
            if carry != 0:
                sum_list = Node(carry, sum_list)
            return reverse_list(sum_list)
        elif n1 == None:
            val, carry = add_digits(n2.data, carry)
            n2 = n2.next
        elif n2 == None:
            val, carry = add_digits(n1.data, carry)
            n1 = n1.next
        else:
            val, carry = add_digits(n1.data, n2.data, carry)
            n1 = n1.next
            n2 = n2.next
        sum_list = Node(val, sum_list)

def add_digits(d1, d2, d3=0):
    val = d1 + d2 + d3
    carry = 0
    while val >= 10:
        carry+=1
        val-=10
    return val, carry

def reverse_list(node):
    curr = node
    prev = None
    while curr != None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev
"""

def num_to_list(num):
    arr = [int(i) for i in str(num)]
    head = None
    for el in arr:
        head = Node(el, head)
    return head

def list_to_num(node):
    num, place, curr = 0, 1, node
    while curr != None:
        num += (place * curr.data)
        curr = curr.next
        place *= 10
    return num

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

l1 = num_to_list(9999)
l2 = num_to_list(2508)
l3 = add_lists(l1, l2)
print(list_to_num(l3))

l1 = num_to_list(9999)
l2 = num_to_list(3)
l3 = add_lists(l1, l2)
print(list_to_num(l3))

l1 = num_to_list(3)
l2 = num_to_list(9999)
l3 = add_lists(l1, l2)
print(list_to_num(l3))

l1 = num_to_list(9999)
l2 = num_to_list(999)
l3 = add_lists(l1, l2)
print(list_to_num(l3))

l1 = num_to_list(1234)
l2 = num_to_list(123)
l3 = add_lists(l1, l2)
print(list_to_num(l3))

l1 = num_to_list(9123)
l2 = num_to_list(9000)
l3 = add_lists(l1, l2)
print(list_to_num(l3))
