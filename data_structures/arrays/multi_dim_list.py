# properly initialize a two-dimensional list
c = 5
r = 3
data = [[0]*c for j in range(r)]
print(data)

# same as above but less efficient since not using list comprehension
d = []
for i in range(3):
    d.append([0]*5)

print(d)
        