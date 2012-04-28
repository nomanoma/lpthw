#-- coding: UTF-8 --
def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multipy(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d"% (a, b)
    return a / b


print "Let's do some math with just function!"

age = add(30, 5)
height = subtract(78, 4)
weight = multipy(90, 2)
iq = divide(100, 2)

print "Age: %d, Height %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multipy(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

# посчитаем (80 - 92) * 18 / (35 + 10)
print "(80 - 92) * 18 / (35 + 10) = %d\n" % divide(multipy(subtract(80, 92), 18), add(35, 10))
