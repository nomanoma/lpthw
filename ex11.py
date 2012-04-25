#-- coding: UTF-8 --
print "How old are you?",
# присвоим переменной age строчку со ввода, преобразованную в строку
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)
