# import argv module from sys
from sys import argv

# unpack script name and argument
script, filename = argv

# open file
txt = open(filename)

# print message about file we'll print
print "Here's your file %r:" % filename
# print file on screen
print txt.read()
# close file
txt.close()

# print new filename request
print "Type the filename again:"
# get new filename from user
file_again = raw_input("> ")

# open new file
txt_again = open(file_again)

# print file on screen
print txt_again.read()
# close new file
txt_again.close()
