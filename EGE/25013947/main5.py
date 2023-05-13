# https://kompege.ru/variant?kim=25013947
def dec_to_bin(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    if n > 1:
        return dec_to_bin(n // 2) + str(n % 2)
    
def F(n):
    sum_nums = 0
    for i in n:
        sum_nums += int(i)
    if sum_nums % 2 == 0:
        n = list(n)
        n.insert(0, "10")
        n[-1] = "0"
        n[-2] = "0"
        a = "".join(n)
    else:
        n = list(n)
        n.insert(0, "11")
        n[-1] = "1"
        n[-2] = "1"
        a = "".join(n)
    return a
b = []
for i in range(30):
    b.append(F(dec_to_bin(i)))
    
print(int(max(b),2))
    