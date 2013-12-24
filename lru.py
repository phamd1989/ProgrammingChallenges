# this is to solve the LRU Cache challenge from Box
# the idea is to use doubly linked list to store all items in the cache
# so Bound and Set is gonna be O(1)
# together with a dictionary to store key-value pair where value is 
# a node in the linked list
# to make sure that Get and Peek gonna be O(1)


class Node(object):
    """This creates a Node object of the linked list.
    """
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
    
    def set_next(self, next):
        """Set the next pointer.
        
        Args:
            next: the next Node this points to
        """
        self.next = next
    
    def set_prev(self, prev):
        self.prev = prev
        

class DoubleLinkedList(object):
    """The double linked list to store all items in the cache
    """
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.curr_size = 0

    def insert_to_head(self, node):
        """Adds this node to the head of the linked list.
        
        Args:
            node: a new node to be inserted into the list
        """
        # node.set_next(self.head)
        # if head is not None, then set the left node on head to node
        if self.head is not None:
            node.set_next(self.head)
            self.head.prev = node
            self.head = node       
        else:
            self.head = node
            self.tail = self.head
        self.curr_size += 1

    def remove(self, node):
        """Remove this node from the linked list.
        """
        # if node is at head
        if node == self.head:
            # change the head node
            self.head = node.next
            # if the new head is not null, set the prev node to be null
            if self.head is not None:
                self.head.prev = None
        # if node is at tail
        elif node == self.tail:
            self.tail = node.prev
            if self.tail is not None:
                self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.curr_size -= 1
        return node

    def maintain(self):
        last_node = self.tail
        self.remove(last_node)
        return last_node.key

class LRUCache(object):
    
    def __init__(self):
        self.double_linked_list = DoubleLinkedList()
        self.cache = {}
        self.bound = 0
    
    def set_bound(self, bound):
        self.bound = bound
        # remove all elements that are not in the cache here
        while self.double_linked_list.curr_size > self.bound:
            key = self.double_linked_list.maintain()
            del self.cache[key]

    def set(self, key, value):
        # removes an existing key
        if key in self.cache:
            self.double_linked_list.remove(self.cache[key])
        # inserts a new node to the cache
        node = Node(key, value)
        self.cache[key] = node
        if self.double_linked_list.curr_size == self.bound:
            key = self.double_linked_list.remove(self.double_linked_list.tail).key
            del self.cache[key]
        self.double_linked_list.insert_to_head(node)

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.double_linked_list.remove(node)
            self.double_linked_list.insert_to_head(node)
            print node.value
        else:
            print 'NULL'
    
    def peek(self, key):
        if key in self.cache:
            print self.cache[key].value
        else:
            print 'NULL'
    
    def dump(self):
        cache_keys = sorted(self.cache.keys())
        for key in cache_keys:
            print key, self.cache[key].value

def main():
    # get the number of commands
    n = int(raw_input())
    # initialize the cache
    lru = LRUCache()
    while (n>0):
        line = raw_input()
        line_data = line.split(' ')
        command = line_data[0]
        if command == 'BOUND':
            lru.set_bound(int(line_data[1]))
        elif command == 'SET':
            key = line_data[1]
            value = line_data[2]
            lru.set(key, value)
        elif command == 'GET':
            key = line_data[1]
            lru.get(key)
        elif command == 'PEEK':
            key = line_data[1]
            lru.peek(key)
        elif command == 'DUMP':
            lru.dump()
        n -= 1

main()