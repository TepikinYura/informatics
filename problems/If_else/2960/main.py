num = int(input())
d = num % 10
c = num // 10 % 10
b = num // 100 % 10
a = num // 1000
x = a * 10 + b
y = d * 10 + c 
print(abc(x - y) + 1)