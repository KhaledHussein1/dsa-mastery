

class LinkedStack:
    """LIFO Stack implementation using a singly linked list for storage"""
    
    #------------nested _Node class---------------
    class _Node:
        '''Lightweight, nonpublic class for sotring a singly linekd node'''
        __slots__ = '_element', '_next' #streamline memory usage

        def __init__(self, element, next):
            self._element = element
            self._next = next
    
    #------------stack methods-----------------
    def __init__(self):
        """Create an empty stack"""
        self._head = None
        self._size = 0
    
    def __len__(self): #O(1)
        """Return the number of elements in the stack"""
        return self._size
    
    def is_empty(self): #O(1)
        return self._size == 0
    
    def push(self, e): #O(1)
        """Add element e to the top of the stack"""
        self._head = self._Node(e, self._head) # create and link new node
        self._size += 1

    def top(self): #O(1)
        """Return (not remove) element at top of stack"""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element 
    
    def pop(self): #O(1)
        """Remove and return element at the top of stack"""
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer
    
    def __str__(self):
        values = []
        current = self._head

        while current:
            values.append(str(current._element))
            current= current._next
        return '-->'.join(values)

if __name__ == '__main__':
    ls = LinkedStack()
    ls.push(4)
    ls.push(3)
    ls.push(2)
    ls.push(1)
    print(ls)
    print(ls.top())
    print(ls.pop())
    print(ls.top())
    print(f'size of linked stack: {len(ls)}')
    print(ls)