#-- coding: UTF-8 --
# присвоим переменной строчку с табуляцией
tabby_cat = "\tI'm tabbed in."
# присвоим переменной строчку в переводом строки
persian_cat = "I'm split\non a line."
# присвоим переменной строчку с двумя слешами
backslash_cat = "I'm \\ a \\ cat."

# присвоим переменной несколько строчек
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip \n\t* Grass
"""

# распечатаем все переменные
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# попробуем ''' вместо """
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip \n\t* Grass
'''
# распечатаем то, что получилось
print fat_cat

# сделаем движущуюся строчку
while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i, 
