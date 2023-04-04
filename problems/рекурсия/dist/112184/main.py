#https://informatics.msk.ru/mod/statements/view.php?id=11221&chapterid=112184#1
# Задача №112184. Шестнадцатеричный код
# Напишите программу, которая переводит переданное её целое число (возможно, отрицательное) в шестнадцатеричный код. Используйте процедуру.
# 
# Входные данные
# Входная строка содержит целое число N .
# 
# Выходные данные
# Программа должна вывести шестнадцатеричное представление переданного её числа.
#str(number % 16)
def fund(n):
    if n < 10:
        return str(n)
    if n <= 10:
        return "A"
    if n <= 11:
        return "B"
    if n <= 12:
        return "C"
    if n <= 13:
        return "D"
    if n <= 14:
        return "E"
    if n <= 15:
        return "F"
def F(number):
    if number == 0:
        return ""
    return F(number // 16) + fund(number % 16)

    
print(F(int(input())))