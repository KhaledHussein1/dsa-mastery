import ctypes

class DynamicArray:
    """A dynammic array class akin to a simplified Python list."""

    def __init__(self):
        """Create an empty array"""
        self._n = 0 # count actual elements
        self._capacity = 1  # default array capacity
        self._A = self._make_array(self._capacity) # low-level array

    def __len__(self):
        """Return number of elements stored in the array"""
        return self._n

    def __getitem__(self, k):
        """Return element at index k"""
        if not 0<=k < self._n:
            raise IndexError('invalid index')
        return self._A[k]   # retrieve from array
    
    def append(self, obj):
        """Add object to end of the array"""
        if self._n == self._capacity:   #not enough room
            self._resize(2*self._capacity) # so double capacity
        self._A[self._n] = obj
        self._n += 1
    
    def _resize(self, c):   # nonpublic utility
        """Resize internal array to capacity c"""
        B = self._make_array(c) # new (bigger) array
        for k in range(self._n):    # for each existing value
            B[k] = self._A[k]
        self._A = B     # use the bigger array
        self._capacity = c
    
    def _make_array(self, c):
        """Return new array with capacity c."""
        return (c * ctypes.py_object)()
    
    def insert(self, k, value):
        """Insert value at index k, shifting subsequent values rightward."""
        # (for simplicity, we assume 0 <= k <= n)
        if self._n == self._capacity:
            self._resize(2*self._capacity)
        for j in range(self._n, k , -1):    #shift rightmost first
            self._A[j] = self._A[j-1]
        self._A[k] = value  # store newest element 
        self._n += 1
    
    def remove(self, value):
        """Remove first occurance of value (or raise ValueError)."""
        # note: not considering shrinking the dynamic array in this version
        for k in range(self._n): 
            if self._A[k] == value: # match found
                for j in range(k, self._n -1): # shift others to fill gap
                    self._A[j] = self._A[j+1]
                self._A[self._n - 1] = None # help garbage collection
                self._n -= 1    # one less item
                return  
        raise ValueError('value not found')

if __name__ == '__main__':
    d_array = DynamicArray()
    d_array.append(5)
    print(d_array.__len__())
    print(d_array.__getitem__(0))
    print(d_array._capacity)
    d_array.append(4)
    print(d_array._capacity)
    d_array.append(3)
    d_array.append(2)
    d_array.append(1)
    print(d_array._capacity)
    print("----------------")
    d_array.insert(2, 44)
    for i in d_array:
        print(i)
    
    print('-------------------')
    d_array.remove(5)
    for i in d_array:
        print(i)