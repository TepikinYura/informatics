#https://informatics.msk.ru/mod/statements/view.php?id=11221&chapterid=112183#1
# Задача №112183. Восьмеричный код
# Напишите программу, которая переводит переданное её целое число (возможно, отрицательное) в восьмеричный код. Используйте процедуру.
# 
# Входные данные
# Входная строка содержит целое число N .
# 
# Выходные данные
# Программа должна вывести восьмеричное представление переданного её числа.
def F(number):
    if 8 > number:
        return str(number) 
    return F(number // 8) + str(number % 8)
def add_minus(n):
    n = int("-" + str(n))
    return n

def chek(n):
    if(n >= 0):
        return F(n)
    if(n < 0):
        return add_minus(F(abs(n)))



print(chek(int(input())))