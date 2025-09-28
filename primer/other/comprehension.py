'''
Comprehension Syntax

[expression for value in iterable if condition]

logically equivalent to:

result = []
for value in iterable:
	if condition:
		result.append(expression)
'''

# List of squares of numbers from 1 to n
n = 10
squares = []
for k in range(1, n+1):
	squares.append(k*k)

squares_2 = [k*k for k in range(1, n+1)]

print('without list comprehension:')
print(squares)
print('with list comprehension:')
print(squares_2)

'''
[ k*k for k in range(1, n+1)] list comprehension
{ k*k for k in range(1, n+1)} set comprehension
( k*k for k in range(1, n+1)) generator comprehension
{ k : k*k for k in range(1, n+1)} dictionary comprehension

NOTE:
To compute the sums of the first n squares, the generator syntax is preferred to 
the use of an explicitly instantiated list comprehension as the parameter since
it does not need to be stored in memory.
'''
