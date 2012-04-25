from sys import argv

script, user_name, pet = argv
prompt = 'noma yee, noma noma noma yee\'!! '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where it is.
You have %r pet.
And you have %r computer. Nice.
""" % (likes, lives, pet, computer)
