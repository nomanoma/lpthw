#-- coding: UTF-8 --
# сделаем строковую переменную которая будет распечатывать любые 4 значения, преобразовав их в строки
formatter = "%r %r %r %r"

# распечатаем цифры
print formatter % (1, 2, 3, 4)
# распечатаем слова
print formatter % ("one", "two", "free", "four")
# распечатаем булевы выражения
print formatter % (True, False, False, True)

# распечатаем содержание четырех строковых переменных
# при этом сами переменные будут преобразованы в строки, и подстановки не будут выполняться
print formatter % (formatter, formatter, formatter, formatter)
# распечатаем несколько строк
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

