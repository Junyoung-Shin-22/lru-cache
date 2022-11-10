from dataclasses import dataclass

@dataclass
class Node:
    key: any
    data: any
    left: any = None
    right: any = None


@dataclass
class DoubleLinkedQueue:
    front: any = None
    rear: any = None
    len: int = 0

    def _pop(self, node):
        if node is self.front:
            self.front = node.right
        
        if node is self.rear:
            self.rear = node.left
        
        if node.left:
            node.left.right = node.right
        if node.right:
            node.right.left = node.left
        
        node.left, node.right = None, None
        self.len -= 1

        return node
    
    def add_rear(self, node):
        node.left = self.rear
        node.right = None

        if self.rear:
            self.rear.right = node
        
        if not self.front:
            self.front = node

        self.rear = node
        self.len += 1
    
    def remove_front(self):
        self._pop(self.front)
    
    def move_to_rear(self, node):
        node = self._pop(node)
        self.add_rear(node)

    def __str__(self):
        s = ''
        node = self.front

        while node:
            s += '-' + str(node.key)
            node = node.right
        
        s += '-'
        return s
        

class LRUCache:
    def __init__(self, size):
        self.size = size
        self.queue = DoubleLinkedQueue()
        self.table = dict()
    
    @classmethod
    def new(cls, size):
        return cls(size)
    
    def get(self, key):
        if key not in self.table:
            raise KeyError(f'no such data with key=={key} in the cache.')
        
        node = self.table[key]
        self.queue.move_to_rear(node)

        return node.data

    def insert(self, key, data):
        # update
        if key in self.table:
            node = self.table[key]
            node.data = data
        
        # add new data
        else:
            node = Node(key, data)

            if self.queue.len == self.size:
                self.table.pop(self.queue.front.key)
                self.queue.remove_front()
            
            self.table[key] = node
            self.queue.add_rear(node)
    
    def __str__(self):
        return str(self.queue)