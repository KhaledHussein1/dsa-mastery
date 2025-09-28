f = open('text.txt', 'r+')

def read(f):
	print('----------------\nOriginal Content:*\n----------------')
	# Move pointer back to the beginning
	f.seek(0)
	# Return the (remaining) contents of a readable file as a string.
	print(f.read())

def get_next_k_bytes(f, k):
	print('----------------\nNext k Bytes:*\n----------------')
	f.seek(0)
	#  Return the next k bytes of a readable file as a string. 1 letter = 1 byte
	print(f.read(k))

def read_line(f):
	print('----------------\nRead Line:*\n----------------')
	f.seek(0)
	#Return (remainder of) the current line of a readable file as a string.
	print(f.readline())

def read_lines(f):
	print('----------------\nRead Lines:*\n----------------')
	f.seek(0)
	# Return all (remaining) lines of a readable file as a list of strings.
	print(f.readlines())

def iterate_lines(f):
	print('----------------\nIterate Lines:*\n----------------')
	f.seek(0)
	#  Iterate all (remaining) lines of a readable file.
	for line in f:
	    print(line, ' - loop')

def get_position(f):
	print('----------------\nGet Position:*\n----------------')
	# Return the current position, measured as byte-offset from the start.
	print(f.tell())

def write(f):
	# Write given string at current position of the writable file.
	f.write("Wow!")

def write_sequence(f):
	'''
	 Write each of the strings of the given sequence at the current
	 position of the writable file. This command does not insert
	 any newlines, beyond those that are embedded in the strings.
	'''
	f.writelines(["sequence", " to add \n", "to the file \n"])
	f.seek(0)
	print(f.read())

def redirect_output(f):
	response = input('What would you like to save to the file?')
	print(response, file = f)

# Test
read(f)
get_next_k_bytes(f, 8)
read_line(f)
read_lines(f)
iterate_lines(f)
get_position(f)
redirect_output(f)
