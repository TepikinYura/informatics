def dec_to_bin(num, base):
    s ="";
    while num > 0:
        s = str(num % base) + s
        num //= base
    return s
print(dec_to_bin(12, 3))