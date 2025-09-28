# Right side can be any iterable type, as long as num of var on left matches
a, b, c, d, e = range(5, 10) # unpack
print(a, b, c, d, e) # a = 5, b = 6, c = 7, d = 8

# Automatic packing
data = 2, 4, 6, 8 #  turns into the tuple (2, 4, 6, 8)

# Can be used in loops
for x, y in [(7,2),(5,6),(9,8)]:
	print(f"({x},{y})")

'''
Commonly used to iterate through key-value pairs that are returned 
by the items() method of the dict class: for k,v in mapping.items()
'''

# Simultaneous Assignments 
x, y, z = 6, 2, 5

j, k = 1, 2
j, k = k, j # perfect for swapping without temp variable!
