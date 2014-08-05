#importing a thing from a pack
from sys import argv
# defining the inputs from powershell through argv 
script, filename = argv
#opneing the file, (defined through argv)
txt = open(filename)
#printing using %r and the file 
print "Here's your file %r: " % filename
print txt.read()

#printing the file thorugh user inpput
print "Type the filename again:"
file_again = raw_input("> ")
#opening the file through raw input
txt_again = open(file_again)

print txt_again.read()
