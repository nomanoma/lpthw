#-- coding: UTF-8 --
# импортируем модуль argv из модуля sys
from sys import argv

# развернем параметры скрипта в переменные
script,filename = argv

# выведем предупреждение о затирании файла
print "We're going to erase %r." % filename
# предложим отменить
print "If you don't want that, hit CTRL+C (^C)."
# если или продолжить
print "If you do want that, hit RETURN."

# если введено что угодно кроме CTRL+C, то продолжим
raw_input("?")

# скажем, что открываем файл
print "Opening the file..."
# откроем файл
target = open(filename, 'w')

# скажем, что очищаем файл (не нужно, при режиме 'w' файл очищается автоматом
#print "Truncating the file. Goodbye!"
# очистим файл
#target.truncate()

# скажем, что нужно ввести три строчки
print "Now I'm going to ask you for three lines."

# спросим первую строчку
line1 = raw_input("line 1: ")
# спросим вторую строчку
line2 = raw_input("line 2: ")
# спросим третью строчку
line3 = raw_input("line 3: ")

# скажем, что собираемся записать эти строчки в файл
print "I'm going to write these to the file."

# запишем все строчки
target.write("%s\n%s\n%s\n" % (
    line1, line2, line3))

# скажем, что закрываем файл
print "And finally, we close it."
# закроем файл
target.close()
