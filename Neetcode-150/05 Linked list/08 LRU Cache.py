# Title: LRU Cache
# Link: https://neetcode.io/problems/lru-cache
# Difficulty: Medium 
# Tags: Linked List

class Node:
    def __init__(self, key = None, value = None, next = None, prev = None):
        self.key = key
        self.value = value
        # Use doubly-linked list
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        # Track the key-value pair -- O(1) lookup
        self.cache = {}
        # Remember the capacity
        self.capacity = capacity
        # Track the LRU-MRU items
        self.lru = Node()
        self.mru = Node()
        # Make the nodes point to each other
        self.lru.next = self.mru
        self.mru.prev = self.lru
    
    def remove(self, node):
        # Remove the node
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insert(self, node):
        # Insertion always happens from the right-end
        # or the MRU end.
        # Eg: 
        #   LRU-node <-> some_nodes ... <-> MRU <-> MRU-node
        # becomes:
        #   LRU-node <-> some_nodes ... <-> (old) MRU <-> node (MRU) <-> MRU-node
        # Insert the node between the MRU and the dummy
        # MRU node.
        node.prev = self.mru.prev
        node.next = self.mru
        # Make the old MRU point to node
        self.mru.prev.next = node
        # Make the node point to MRU dummy node
        self.mru.prev = node


    def move_to_mru(self, node):
        # Remove from the list
        self.remove(node)
        # Insert before the MRU-node
        self.insert(node)
    
    def get(self, key: int) -> int:
        
        # If the key already exists
        if key in self.cache.keys():
            # Get the node
            node = self.cache[key]
            # Progress it to the MRU
            self.move_to_mru(node)
            # Return the value
            return node.value
        # If the key doesn't exist in the cache
        return -1

    def put(self, key: int, value: int) -> None:

        # If the key already exists
        if key in self.cache.keys():
            # Get the node
            node = self.cache[key]
            # Update the value
            node.value = value
            # Move the node to MRU
            self.move_to_mru(node)
            return
        
        # If capacity is reached
        if len(self.cache) == self.capacity:
            # Get the LRU item
            lru = self.lru.next
            # Remove it from the cache
            self.cache.pop(lru.key)
            # Remove it from the list
            self.remove(lru)
        
        # If the key doesn't exist, create a new node
        node = Node(key, value)
        # Add it to the cache
        self.cache[key] = node
        # Insert it in the list
        self.insert(node)