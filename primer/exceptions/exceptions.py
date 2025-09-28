# raise triggers an exception intentionally
def raise_zero_division_error(x):
	if x == 0:
		raise ZeroDivisionError('Cannot divide by zero!!!')
	else:
		print('input 0 to raise the exception.')

# create custom exceptions by subclassing Exception
class DontDoThat(Exception):
	'''example of making your own exception'''
	pass

def test_custom_exception():
	raise DontDoThat('Please, don\'t do that again.')


#  try/except - catch and handle errors
def risky():
	x = 9/0
try:
	risky()
except ZeroDivisionError as e:
	print('Handled', e)

# raise inside of except = re-throw after partial handling
# error will propogate upward.
def risky_again():
	y = 9/0

try:
	risky_again()
except ZeroDivisionError as e:
	print('log:', e)
	raise



