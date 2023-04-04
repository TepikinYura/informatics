def F(number, scale):
    num1 = abs(number)
    if scale > num1 and number > 0:
        return str(num1)
    if number < 0  and scale > num1:
        return "-" + str(num1)
    return F(number // scale, scale) + str(number % scale)
a, b = list(input().split())
print(F(int(a), int(b)))