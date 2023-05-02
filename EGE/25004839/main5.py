def dec_to_bin(n):
    s ="";
    while n > 0:
        s = str(n % 2) + s
        n //= 2
    return s
def dec_to_add(s):
    summ = 0
    for i in s:
        summ += int(i)
    d = summ % 2
    s = s + str(d) + str(d)
    s = int(s,2)
    return s
for i in range(100):
    if dec_to_add(dec_to_bin(i)) > 77:
        print(i)
        break
