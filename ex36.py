#--coding: UTF-8--
import sys, random

def main():
    guessed = 0
    while number != guessed:
        try:
            guessed = int(raw_input("Enter a number>"))
            compare(guessed)
        except ValueError, e:
            print "%r is not a number. Try again, would you?" % guessed
            pass
        except KeyboardInterrupt, e:
            print "\nGood bye than."
            sys.exit()

def compare(guessed):
    if guessed == number:
        print "You guessed a number! Good job!"
    elif guessed > number:
        print "Number is larger than you specified, try again."
    elif guessed < number:
        print "Number is smaller than you specified, try again."
    else:
        print "Something bad happaned, guessed = %r. Good job!" % guessed

print "Just a game of guessing a number"
number = int(random.randint(1,100))
main()
