class LinkedCircularQueue:
    """Queue implementation using circularly linked list for storage"""
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next
        
    def __init__(self):
        self._tail = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        head = self._tail._next
        return head._element
    
    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        oldhead = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = oldhead._next
        self._size -= 1
        return oldhead._element
    
    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1
    
    def rotate(self):
        """Rotate front element to the back of queue"""
        if self._size > 0:
            self._tail = self._tail._next # old head becomes new tail



    
if __name__ == '__main__':
    lq = LinkedCircularQueue()
    lq.enqueue(1)
    lq.enqueue(2)
    lq.enqueue(3)
    lq.enqueue(4)

    print(lq.first())

    print(len(lq))

    print(lq.dequeue())

    print(lq.first())
    lq.rotate()

    print(lq.first())


