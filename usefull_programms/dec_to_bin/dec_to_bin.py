def dec_to_bin(n):
    s ="";
    while n > 0:
        s = str(n % 2) + s
        n //= 2
    return s
print(dec_to_bin(12))