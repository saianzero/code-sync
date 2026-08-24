class LRUCache:

    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # Dummy nodes
        self.head = self.Node(-1, -1)  # MRU side
        self.tail = self.Node(-1, -1)  # LRU side

        # construct the DLL structure
        self.head.next = self.tail
        self.tail.prev = self.head

    # Add node immediately after head
    def add_to_front(self, node: "Node") -> None:
        # Get the current first node after head
        first_node = self.head.next
        
        # Link: head <-> node <-> first_node
        node.prev = self.head
        node.next = first_node
        self.head.next = node
        first_node.prev = node

    # Remove node from wherever it is
    def remove_node(self, node: "Node") -> None:
        # Get the neighbors
        prev_node = node.prev
        next_node = node.next
        
        # Bypass this node: prev <-> next
        prev_node.next = next_node
        next_node.prev = prev_node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]

        # Accessed: becomes most recently used
        self.remove_node(node)
        self.add_to_front(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        # If key already exists, update value and move to front
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove_node(node)
            self.add_to_front(node)

            return
        
        # If cache is full, remove LRU node
        if len(self.cache) == self.capacity:
            lru_node = self.tail.prev
            self.remove_node(lru_node)
            del self.cache[lru_node.key]
        
        # Add new node as MRU
        new_node = self.Node(key, value)
        self.add_to_front(new_node)
        self.cache[key] = new_node