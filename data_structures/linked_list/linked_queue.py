class LinkedQueue:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element 
            self._next = next
    
    def __init__(self):
        """create empty queue"""
        self._head = None
        self._tail = None
        self._size = 0
    
    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty.')
        return self._head._element
    
    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty.")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer
    
    def enqueue(self, e):
        n = self._Node(e, None)
        if self.is_empty():
            self._head = n
        else:
            self._tail._next = n
        self._tail = n
        self._size += 1
    
    def __str__(self):
        values = []
        current = self._head
        while current:
            values.append(str(current._element))
            current = current._next
        return "-->".join(values)

if __name__ == '__main__':
    lq = LinkedQueue()
    lq.enqueue(1)
    lq.enqueue(43)
    lq.enqueue(21)
    lq.enqueue(2)
    print(lq)
    print(lq.first())
    print(len(lq))
    print(lq.dequeue())
    print(lq)
