#-- coding: UTF-8 --

def call_me(animal, number_of_animals):
    print "You have %d of %s animal" % (
        number_of_animals, animal)

# вызовем функцию напрямую
call_me("dog", 10)

# используем математическую операцию
call_me("dog", 10*9)

# используем сложение строк
call_me("lazy + dog", 10)

# используем математическую операцию и сложение строк
call_me("lazy + dog", 10*9)

# сделаем переменные для параметров
animal = "dog"
number = 100

# вызовем, пердав параметры через переменную
call_me(animal, number)

# совместим передачу через переменную и математическую операцию
call_me(animal, number + 100)

# совместим передачу через переменную и сложение строк
call_me("lazy" + animal, number)

# совместим передачу через переменную, сложение строк и математическую операцию
call_me("lazy" + animal, number + 100)

# вызовем еще вот так
call_me(animal + "very " + "lazy ", 999)

# и вот так
call_me(animal*10, 768)


