n = input()
def F(n):
    if not n:
        return 0
    else:
        return (not int(n[0]) % 2) + F(n[1:])
print(F(n))