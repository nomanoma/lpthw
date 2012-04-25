from sys import argv

script, first, second, third = argv

print "This script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

test = raw_input("gimme gimme!! ")

print "1 %r, 2 %r, 3 %r, 4 %r, 5 %s" % (
    script, first, second, third, test)
