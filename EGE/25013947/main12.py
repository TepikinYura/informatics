#https://kompege.ru/variant?kim=25013947
a = ">1111111111111111111111111222222222222222223333333333"
while(">1" in a) or (">2" in a) or (">3" in a):
    if ">1" in a:
        a = a.replace(">1", "22>3",1)
    if ">2" in a:
        a = a.replace(">2", "2>", 1)
    if ">3" in a:
        a = a.replace(">3", "11>2", 1)
a = a.replace(">", "0", 1)
count = 0
for i in a:
    count += int(i)
print(a, count)
        