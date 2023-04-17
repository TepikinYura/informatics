a = [0] * 10010
for i in range(10000, 10010):
    a[i] = i
for i in range(9999,-1,-1):
    if i % 2 == 0:
        a[i] = a[i + 2] - 3
    else:
        a[i] = a[i + 2] + 1
print(a[94] - a[80])