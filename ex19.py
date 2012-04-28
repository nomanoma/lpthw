#-- coding: UTF-8 --
# сделаем функцию, принимающую на вход количство сырков и количество крэкеров
# и распечатывающую их и еще пару строк
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enogh for the party!"
    print "Get a blanket.\n"


# вызовем функцию передав числа прямо
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# вызовем функцию, передав параметры через переменные
print "OR, we can use variables from out script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# вызовем функцию, используя математические операции при передаче параметров
print "We can even do the math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# вызовем функцию, передав параметры с которыми при передаче совершаются математические операции
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
