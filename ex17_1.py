from sys import argv
from os.path import exists 

script, from_file, to_file = argv 

print "\nCopying from %s to %s\n"% (from_file, to_file)

# we could do these two on one line too, wie?
in_file, indata = open(from_file)

out_file = open(to_file, 'w') # "w" is an IDer for write
out_file.write(indata) 

out_file.close()
in_file.close()
