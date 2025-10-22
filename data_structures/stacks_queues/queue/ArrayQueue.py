class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

class ArrayQueue:
    """FIFO queue implementation (circular array) using a python list as underlying storage"""
    DEFAULT_CAPACITY = 10 

    def __init__(self):
        """Create an empty queue."""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self): # O(1)
        """Return the number of elements in the queue"""
        return self._size

    def is_empty(self): # O(1)
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self): # O(1)
        """Return (not remove) the element at the front of the queue.

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty(): 
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self): # O(1) amortized
        """Remove and return the first element of the queue

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None  # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        # reduce the array to half of its current size, when # elements stored in it fals below 1/4 of capacity.
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer
    
    def enqueue(self, e): # O(1) amortized
        """Add an element to the back of the queue."""
        if self._size == len(self._data):
            self._resize(2*len(self.data))  # double the array size
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1 
    
    def _resize(self, cap): # we assume cap>= len(self)
        """Resize to a new list of capacity >= len(self)"""
        old = self._data    # keep track of existing list
        self._data = [None] * cap   # allocate list with new capacity
        walk = self._front
        for k in range(self._size): # only consider existing elements
            self._data[k] = old[walk]   #intentionally shift indices
            walk = (1 + walk) % len(old)    # use old size as modulus
        self._front = 0

if __name__ == '__main__':
    Q = ArrayQueue()
    Q.enqueue(5)
    Q.enqueue(3)
    len(Q)
    Q.dequeue()
    Q.is_empty()
    Q.dequeue()
    Q.is_empty()
    # Q.dequeue()
    Q.enqueue(7)
    Q.enqueue(9)
    Q.first()
    Q.enqueue(4)
    len(Q)
    Q.dequeue()
