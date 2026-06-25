
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None 
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        #dummy nodes 
        self.right = Node(0, 0)
        self.left = Node(0, 0)

        self.right.prev = self.left
        self.left.next = self.right

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt 
        nxt.prev = prev
    
    def insert(self, node):
        prev = self.right.prev
        nxt = self.right
        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node 
        self.insert(node)
        
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

