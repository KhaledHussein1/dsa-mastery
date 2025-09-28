# Embedding formal documenation in source code

# Any string literal that appears as the first statement
# within a body of a module, class, or function is a docstring.
def scale(data, factor):
	'''Multiply all entries of numeric data list by the given factor.

	data	an instance of any mutable sequence type (such as list)
		containing numeric elements

	factor	a number that serves as the multiplicative factor for scaling
	'''
	for j in range(len(data)):
		data[j] *= factor

# can use to retrieve docstring - help(x)
help(scale)

# pydoc comes with python and can be used to generate doc as text or web page.




