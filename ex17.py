from sys import argv
from os.path import exists 

script, from_file, to_file = argv 

print "\nCopying from %s to %s\n"% (from_file, to_file)

# we could do these two on one line too, wie?
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long\n" % len(indata)

print "Does the output file exist? %r\n" % exists(to_file)
print "Ready, hit RETURN to continue, CTRC-C to abort."
raw_input()

out_file = open(to_file, 'w') # "w" is an IDer for write
out_file.write(indata) 

print "Alright, all done."

out_file.close()
in_file.close()

""" Line 19 is where we copy stuff from "from" to "to"
	but what happens if we have data already in "to"
	we didnt truncate, questions, questions.
	UPDATE: It overrides"""
	
	
	