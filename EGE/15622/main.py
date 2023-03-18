#ЕГЭ  №15622
def dec_to_bin(n):
    s = ""
    while(n > 0):
        s = str(n % 2) + s
        n //= 2
    return s

def add_two_num(n, s):
    count = 0
    for i in s:
        count += int(i)
    if count % 2 == 0:
        s = s + "00"
    else:
        s = s + "11"
    return s

for i in range(1000):
    num = add_two_num(i, dec_to_bin(i))
    num = int(num, 2)
    if num > 114:
        print(num)
        break
    