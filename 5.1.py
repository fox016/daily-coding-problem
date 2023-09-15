"""
Implement an LRU (least recently used) cache
Init to size n
On set, if size is n, remove least recently used element
If set is used on existing key, replace value
On get, update least recently used
"""
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:

    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def pop_front(self):
        head = self.head.next
        if head.key == None:
            raise Exception("No node to pop off")
        self.remove(head)
        return head

    def append(self, node):
        prev = self.tail.prev
        self.tail.prev = node
        node.prev = prev
        prev.next = node
        node.next = self.tail

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

class LRUCache:

    def __init__(self, n):
        self.n = n
        self.list = LinkedList()
        self.dict = {}

    def set(self, key, val):
        if key in self.dict:
            self.list.remove(self.dict[key])
        node = Node(key, val)
        self.dict[key] = node
        self.list.append(node)
        if len(self.dict) > self.n:
            head = self.list.pop_front()
            del self.dict[head.key]

    def get(self, key):
        if key in self.dict:
            node = self.dict[key]
            self.list.remove(node)
            self.list.append(node)
            return node.value
        return None


cache = LRUCache(3)
cache.set("a", "apple")
cache.set("b", "banana")
cache.set("c", "cherry")
cache.set("d", "dog")
print(cache.get("c"))
print(cache.get("a"))
print(cache.get("b"))
print(cache.get("d"))
cache.set("e", "elephant")
print(cache.get("c"))
print(cache.get("e"))
cache.set("e", "eggplant")
cache.set("f", "fox")
print(cache.get("e"))
