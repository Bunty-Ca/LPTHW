from sys import argv 

script, filename = argv

print " Let's play with this file %r." % filename
words = raw_input("> ")
print " Enter something to write in the file"

target = open(filename, 'w')

target.truncate()
target.write(words)
target.close()

testing = open(filename)

print "Let see if it worked!"
print testing.read()

testing.close()


