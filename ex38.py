ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')               # split(' ', stuff), split things with space between them
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()             # pop(more_stuff), take thing from more_stuff and delete it from more_stuff
    print "Adding: ", next_one
    stuff.append(next_one)                  # append('next_one', 'stuff'), add next_one to stuff
    print "There's %d items now." % len(stuff) 

print "There we go: ", stuff

print stuff[1]                              # take first thing from stuff
print stuff[-1]                             # take last thing from stuff
print stuff.pop()                           # pop(stuff), take first thing from stuff and delete it in stuff
print ' '.join(stuff) # what? cool!         # join(' ', stuff), join splitted stuff with spaces as separators
print '#'.join(stuff[3:5]) # super stellar! # join('#', stuff), join splitted stuff from 4 to 5 position, excluding 6th
