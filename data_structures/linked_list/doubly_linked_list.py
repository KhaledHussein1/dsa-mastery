# Implemented with sentinel nodes header and trailer
class _DoubleLinkedBase:
    """Base class providing a doubly linked list representation"""

    class _Node:
        __slots__= '_element', '_prev', '_next' #streamline memory

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next
        
    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def _insert_between(self, e, predecessor, successor):
        """Add element e between two exisiting nodes and return new node"""
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest
    
    def _delete_node(self, node):
        """Delete nonsentinel node from the list and return its element"""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element 
    
    def _iter_forward(self):
        cur = self._header._next
        while cur is not self._trailer:
            yield cur._element
            cur = cur._next

    def __str__(self):
        return "[" + " <-> ".join(
            str(e) for e in self._iter_forward()
        ) + "]"

    
if __name__ == "__main__":
    dll = _DoubleLinkedBase()

    print("Empty?", dll.is_empty(), "len =", len(dll))

    # Insert 3 elements: [10, 20, 30]
    n10 = dll._insert_between(10, dll._header, dll._trailer)
    n20 = dll._insert_between(20, n10, dll._trailer)
    n30 = dll._insert_between(30, n20, dll._trailer)

    print("After inserts, len =", len(dll))

    # Insert at front: [5, 10, 20, 30]
    n5 = dll._insert_between(5, dll._header, dll._header._next)

    print(dll)

    # Delete a middle node (20)
    removed = dll._delete_node(n20)
    print("Removed:", removed)

    # Delete front and back real nodes
    removed_front = dll._delete_node(n5)
    removed_back = dll._delete_node(n30)
    print("Removed front:", removed_front, "Removed back:", removed_back)

    print(dll)