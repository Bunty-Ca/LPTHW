from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()
	#defining a function that prints the entire file, after reading it
def rewind(f):
	f.seek(0)
	#i dont know what this does, probaby goes back to the begining of the file, rather than keep reading on!
def print_a_line(line_count, f):
	print line_count, f.readline()
	#takes two arguments, then prints the line number, then reads the line and prints it
current_file = open(input_file)
#declares the current file as the input file, set by the argv
print "First let's print the whole file: \n"

print_all(current_file)
#calls the print_all func
print "Now let's rewind, kind of like a tape."

rewind(current_file)
#calls the rewind func
print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
#calls the print_a_line func with three diff lines