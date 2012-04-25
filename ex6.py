#-- coding: UTF-8 --
x = "There are %d types of people." % 10                          # строка и число 10
binary = "binary"                                                 # присваивание
do_not = "don't"                                                  # присваивание 
y = "Those who know %s and those who %s." % (binary, do_not)      # строка и две строковых переменных

print x                                                           # распечатать x 
print y                                                           # распечатать y

print "I said: %r." % x                                           # распечатать строку с переменной
print "I also said: '%s'." % y                                    # распечатать строку и еще переменную

hilarious = False                                                 # присвоить булево значение
joke_evaluation = "Isn't this joke so funny?! %r"                 # строка с переменной "распечатать все"

print joke_evaluation % hilarious                                 # распечатать строку

w = "This is left side of..."                                     # левая часть строки
e = "a string with a right side."                                 # правая часть строки

print w + e                                                       # распечатать обе части
