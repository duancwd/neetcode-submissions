class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        # dummy head and tail
        self.left = Node(0, 0)   # MRU side
        self.right = Node(0, 0)  # LRU side

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        pre_node = node.prev
        next_node = node.next
        pre_node.next = next_node
        next_node.prev = pre_node

    def insert(self, node):

        next_node = self.left.next
        self.left.next = node
        node.prev = self.left
        node.next = next_node
        next_node.prev = node




    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if  key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, value)

        self.cache[key] = node

        self.insert(node)


        if len(self.cache) > self.cap:
            lru = self.right.prev
            self.remove(lru)
            del self.cache[lru.key]







        
