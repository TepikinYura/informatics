#https://informatics.msk.ru/mod/statements/view.php?id=30546&chapterid=3762#1
# Задача №3762. Самое частое слово
# Дан текст (строк может быть много). Выведите слово, которое в этом тексте встречается чаще всего. Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
# 
# Входные данные
# Вводится текст.
# 
# Выходные данные
# Выведите ответ на задачу.



dict = {}
with open("input.txt", "r") as file:
    for line in file:
        words = line.strip().split()
        for i in words:
            dict[i] = dict.get(i, 0) + 1
            
max_value = max(dict.values())
for k,v in dict.items():
    if v == max_value:
        print(k)
