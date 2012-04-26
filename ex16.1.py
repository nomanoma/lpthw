#-- coding: UTF-8 --
from sys import argv

script,filename = argv

print "I'm going to show you the file: %r" % filename
print "I'm opening the file now..."
target = open(filename, 'r')

print "Now I'm printing it on your screen...\n"
print target.read()

print "Now I'll close the file."
target.close()
