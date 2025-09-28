'''
- Generators use 'yield' to return values one at a time, pausing the functions state.
- Memory efficient and lazy sequences (values computed only when needed)
- Good for large datasets or infinite sequences.

1. State is preserved
2. Use next() to manually fetch the next value.
3. Once the generator is exhausted you'll need to make a new generator.

* return - sends a value once and then terminates the function.
* yield - sends a value each time it is called and pauses the function, 
  allowing you to resume from where it left off.
'''

def countdown(n):
    while n > 0:
        yield n  # Pause and return n
        n -= 1    # Decrement n

# Function to get the next few numbers from a generator
def get_next_items(generator, count):
	for _ in range(count):
		try:
			yield next(generator)
		except StopIteration:
			print("StopIteration raised!!!")
			return

counter = countdown(5)

print("""countdown(5)
Get the first 2 numbers:""")
for num in get_next_items(counter, 2):
    print(num)  # Output: 5 4

print('Get the next 2 numbers:')
for num in get_next_items(counter, 2):
    print(num)  # Output: 3 2

print('Get the final number:')
for num in get_next_items(counter, 1):
	print(num)

print("Now the generator is exhausted, nothing else to yield.")
print("Attempting to iterate an exhausted generator raises an exception.")
for num in get_next_items(counter, 1):
	print(num)

