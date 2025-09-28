'''
Conditional Expressions 

expr1 if condition else expr2
'''

n = -8

if n >= 0:
	param = n
else:
	-n

# same as:

param = n if n >= 0 else -n

# note, cond. expr. can serve as a parameter to a function

def some_function(n):
	return n

result = some_function(n if n >= 0 else -n)

print(result)
